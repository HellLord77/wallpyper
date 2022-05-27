from __future__ import annotations as _

import atexit
import builtins
from typing import Any
from typing import Callable
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import TypeVar
from typing import Union

from .. import byref
from .. import enum
from .. import get_winrt
from .. import get_winrt_class_name
from .. import handle
from .. import interface
from .. import lib
from .. import macro
from .. import pointer
from .. import struct
from .. import type

_TUnknown = TypeVar('_TUnknown', bound=interface.IUnknown)


# noinspection PyPep8Naming
class boolean(type.boolean):
    @property
    def value(self) -> bool:
        return bool(super().value)


class HSTRING(handle.HSTRING):
    def __str__(self):
        return self.get_string()

    def __getitem__(self, item):
        if isinstance(self, item):
            return self
        raise KeyError

    @property
    def value(self) -> str:
        return self.get_string()


class _Interface(builtins.type):
    _interfaces: dict[builtins.type[_TUnknown], Optional[_TUnknown]]
    _statics: dict[builtins.type[_TUnknown], Optional[_TUnknown]]
    lib.Combase.RoInitialize(enum.RO_INIT_TYPE.MULTITHREADED)
    atexit.register(lib.Combase.RoUninitialize)

    def __del__(self):  # TODO
        if isinstance(self._statics, dict):
            for static, obj in self._statics.items():
                if obj:
                    obj.Release()
                    self._statics[static] = None

    def __getitem__(self, item: builtins.type[_TUnknown]) -> Optional[_TUnknown]:
        if self._statics[item] is None:
            with get_winrt(item) as obj:
                if obj:
                    obj.AddRef()
                    self._statics[item] = obj
        return self._statics[item]


class _Unknown(metaclass=_Interface):
    _self: Optional[interface.IUnknown] = None
    _release = False
    _statics = {}
    _interfaces = {interface.IUnknown: None}  # FIXME thousands of missing interfaces

    def __init_subclass__(cls):
        cls._statics = {static: None for static in cls._statics}
        # noinspection PyProtectedMember,PyUnresolvedReferences
        cls._statics.update(cls.__base__._statics)
        cls._interfaces = {interface_: None for interface_ in cls._interfaces}
        for base in cls.__mro__:
            if hasattr(base, '_interfaces'):
                # noinspection PyProtectedMember
                cls._interfaces.update({interface_: None for interface_ in base._interfaces})

    def __init__(self, obj: Optional[Union[_Unknown, interface.IUnknown]] = None):
        if isinstance(obj, _Unknown):
            obj = obj._self  # TODO obj.AddRef()
        if obj is None:
            obj = interface.IInspectable()
            lib.Combase.RoActivateInstance(HSTRING.from_string(
                get_winrt_class_name(next(iter(self._interfaces)))), byref(obj))
            self._release = True
        self._self = obj
        self._interfaces = self._interfaces.copy()

    def __del__(self):
        if self._self:
            if self._release:
                self._self.Release()
            self._self = None
            for interface_, obj in self._interfaces.items():
                if obj:
                    obj.Release()
                    self._interfaces[interface_] = None

    def __bool__(self):
        return bool(self._self)

    def __hash__(self):
        return self._self.value

    def __getitem__(self, item: builtins.type[_TUnknown]) -> Optional[_TUnknown]:
        if self._interfaces[item] is None:
            obj = item()
            if macro.SUCCEEDED(self._self.QueryInterface(*macro.IID_PPV_ARGS(obj))):
                self._interfaces[item] = obj
        return self._interfaces[item]

    def add_ref(self) -> bool:
        return macro.SUCCEEDED(self[interface.IUnknown].AddRef())

    def release(self) -> bool:
        return macro.SUCCEEDED(self[interface.IUnknown].Release())


class _Inspectable(_Unknown):
    _interfaces = (interface.IInspectable,)

    def get_iids(self) -> Optional[tuple[str]]:
        count = type.ULONG()
        values = pointer(struct.IID)()
        value = type.LPOLESTR()
        if macro.SUCCEEDED(self[interface.IInspectable].GetIids(byref(count), byref(values))):
            # noinspection PyTypeChecker
            return tuple(value.value for index in range(count.value) if macro.SUCCEEDED(
                lib.Ole32.StringFromIID(values[index], byref(value))))

    def get_runtime_class_name(self) -> str:
        value = HSTRING()
        self[interface.IInspectable].GetRuntimeClassName(byref(value))
        return value.value

    def get_trust_level(self) -> enum.TrustLevel:
        value = enum.TrustLevel()
        self[interface.IInspectable].GetTrustLevel(byref(value))
        return value


class _Closable(_Inspectable):
    _interfaces = (interface.Windows.Foundation.IClosable,)

    def close(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.IClosable].Close())


class _VisualElement(_Inspectable):
    _interfaces = (interface.Windows.UI.Composition.IVisualElement,
                   interface.Windows.UI.Composition.IVisualElement2)


class _AnimationObject(_Inspectable):
    _interfaces = (interface.Windows.UI.Composition.IAnimationObject,)


class _ScrollSnapPointsInfo(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo,)

    @property
    def are_horizontal_snap_points_regular(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo].get_AreHorizontalSnapPointsRegular(byref(value))
        return value.value

    @property
    def are_vertical_snap_points_regular(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo].get_AreVerticalSnapPointsRegular(byref(value))
        return value.value


class _InsertionPanel(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.Controls.IInsertionPanel,)


class RoutedEventArgs(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.IRoutedEventArgs,)

    @property
    def original_source(self) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.IRoutedEventArgs].get_OriginalSource(byref(obj))
        return _Inspectable(obj)


class _IRoutedEventHandler(interface.Windows.UI.Xaml.IRoutedEventHandler_impl):
    function: Callable
    args: Iterable
    kwargs: Mapping[str, Any]

    # noinspection PyPep8Naming
    def Invoke(self, sender: interface.IInspectable, e: interface.Windows.UI.Xaml.IRoutedEventArgs) -> type.HRESULT:
        return self.function(_Inspectable(sender), RoutedEventArgs(e), *self.args, **self.kwargs)


class RoutedEventHandler(_Unknown):  # TODO not releasing
    _interfaces = (interface.Windows.UI.Xaml.IRoutedEventHandler,)

    @classmethod
    def create_instance(cls, function: Callable[[_Inspectable, RoutedEventArgs, ...], type.HRESULT], args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> RoutedEventHandler:
        obj = _IRoutedEventHandler()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return RoutedEventHandler(obj)

    def __call__(self, sender: _Inspectable, e: RoutedEventArgs) -> type.HRESULT:
        return self[interface.Windows.UI.Xaml.IRoutedEventHandler].Invoke(sender[interface.IInspectable], e[interface.Windows.UI.Xaml.IRoutedEventArgs])


class CoreDispatcher(_Inspectable):
    _interfaces = (interface.Windows.UI.Core.ICoreDispatcher,
                   interface.Windows.UI.Core.ICoreDispatcher2)


class DesktopWindowXamlSource(_Closable):
    _interfaces = (interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource,)

    @property
    def content(self) -> UIElement:
        obj = interface.Windows.UI.Xaml.IUIElement()
        self[interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource].get_Content(byref(obj))
        return UIElement(obj)

    @content.setter
    def content(self, value: UIElement):
        self[interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource].put_Content(value[interface.Windows.UI.Xaml.IUIElement])

    @property
    def has_focus(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource].get_HasFocus(byref(value))
        return value.value


class WindowsXamlManager(_Closable):
    _statics = (interface.Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Hosting.IWindowsXamlManager,)

    @classmethod
    def initialize_for_current_thread(cls) -> WindowsXamlManager:
        obj = interface.Windows.UI.Xaml.Hosting.IWindowsXamlManager()
        cls[interface.Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics].InitializeForCurrentThread(byref(obj))
        return WindowsXamlManager(obj)


class DependencyObject(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.IDependencyObjectFactory,)
    _interfaces = (interface.Windows.UI.Xaml.IDependencyObject,
                   interface.Windows.UI.Xaml.IDependencyObject2)


class UIElement(_AnimationObject, _VisualElement, DependencyObject):
    _statics = (interface.Windows.UI.Xaml.IUIElementStatics,
                interface.Windows.UI.Xaml.IUIElementStatics10,
                interface.Windows.UI.Xaml.IUIElementStatics2,
                interface.Windows.UI.Xaml.IUIElementStatics3,
                interface.Windows.UI.Xaml.IUIElementStatics4,
                interface.Windows.UI.Xaml.IUIElementStatics5,
                interface.Windows.UI.Xaml.IUIElementStatics6,
                interface.Windows.UI.Xaml.IUIElementStatics7,
                interface.Windows.UI.Xaml.IUIElementStatics8,
                interface.Windows.UI.Xaml.IUIElementStatics9)
    _interfaces = (interface.Windows.UI.Xaml.IUIElement,
                   interface.Windows.UI.Xaml.IUIElement2,
                   interface.Windows.UI.Xaml.IUIElement3,
                   interface.Windows.UI.Xaml.IUIElement4,
                   interface.Windows.UI.Xaml.IUIElement5,
                   interface.Windows.UI.Xaml.IUIElement7,
                   interface.Windows.UI.Xaml.IUIElement8,
                   interface.Windows.UI.Xaml.IUIElement9,
                   interface.Windows.UI.Xaml.IUIElement10,
                   interface.Windows.UI.Xaml.IUIElementOverrides,
                   interface.Windows.UI.Xaml.IUIElementOverrides7,
                   interface.Windows.UI.Xaml.IUIElementOverrides8,
                   interface.Windows.UI.Xaml.IUIElementOverrides9)

    @classmethod
    @property
    def allow_drop_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_AllowDropProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def opacity_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_OpacityProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def clip_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_ClipProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def render_transform_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_RenderTransformProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def projection_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_ProjectionProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def render_transform_origin_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_RenderTransformOriginProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_hit_test_visible_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_IsHitTestVisibleProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def visibility_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_VisibilityProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def use_layout_rounding_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_UseLayoutRoundingProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def transitions_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_TransitionsProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def cache_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_CacheModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_tap_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_IsTapEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_double_tap_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_IsDoubleTapEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_right_tap_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_IsRightTapEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_holding_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_IsHoldingEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def manipulation_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_ManipulationModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def pointer_captures_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics].get_PointerCapturesProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def shadow_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics10].get_ShadowProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def composite_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics2].get_CompositeModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def transform_3d_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics3].get_Transform3DProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def can_drag_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics3].get_CanDragProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def context_flyout_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics4].get_ContextFlyoutProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def exit_display_mode_on_access_key_invoked_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics4].get_ExitDisplayModeOnAccessKeyInvokedProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_access_key_scope_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics4].get_IsAccessKeyScopeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def access_key_scope_owner_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics4].get_AccessKeyScopeOwnerProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def access_key_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics4].get_AccessKeyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def lights_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_LightsProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_placement_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipPlacementModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_horizontal_offset_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipHorizontalOffsetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_vertical_offset_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipVerticalOffsetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_keyboard_navigation_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusKeyboardNavigationProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_up_navigation_strategy_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusUpNavigationStrategyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_down_navigation_strategy_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusDownNavigationStrategyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_left_navigation_strategy_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusLeftNavigationStrategyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_right_navigation_strategy_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusRightNavigationStrategyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def high_contrast_adjustment_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_HighContrastAdjustmentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def tab_focus_navigation_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics5].get_TabFocusNavigationProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyTipTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_placement_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyboardAcceleratorPlacementTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_placement_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyboardAcceleratorPlacementModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def can_be_scroll_anchor_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IUIElementStatics9].get_CanBeScrollAnchorProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def desired_size(self) -> struct.Windows.Foundation.Size:
        value = struct.Windows.Foundation.Size()
        self[interface.Windows.UI.Xaml.IUIElement].get_DesiredSize(byref(value))
        return value

    @property
    def allow_drop(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_AllowDrop(byref(value))
        return value.value

    @allow_drop.setter
    def allow_drop(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_AllowDrop(value)

    @property
    def opacity(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IUIElement].get_Opacity(byref(value))
        return value.value

    @opacity.setter
    def opacity(self, value: float):
        self[interface.Windows.UI.Xaml.IUIElement].put_Opacity(value)

    @property
    def visibility(self) -> enum.Windows.UI.Xaml.Visibility:
        value = enum.Windows.UI.Xaml.Visibility()
        self[interface.Windows.UI.Xaml.IUIElement].get_Visibility(byref(value))
        return value

    @visibility.setter
    def visibility(self, value: enum.Windows.UI.Xaml.Visibility):
        self[interface.Windows.UI.Xaml.IUIElement].put_Visibility(value)

    @property
    def render_size(self) -> struct.Windows.Foundation.Size:
        value = struct.Windows.Foundation.Size()
        self[interface.Windows.UI.Xaml.IUIElement].get_RenderSize(byref(value))
        return value

    @property
    def use_layout_rendering(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_UseLayoutRounding(byref(value))
        return value.value

    @use_layout_rendering.setter
    def use_layout_rendering(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_UseLayoutRounding(value)

    @property
    def is_tap_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_IsTapEnabled(byref(value))
        return value.value

    @is_tap_enabled.setter
    def is_tap_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_IsTapEnabled(value)

    @property
    def is_double_tap_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_IsDoubleTapEnabled(byref(value))
        return value.value

    @is_double_tap_enabled.setter
    def is_double_tap_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_IsDoubleTapEnabled(value)

    @property
    def is_right_tap_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_IsRightTapEnabled(byref(value))
        return value.value

    @is_right_tap_enabled.setter
    def is_right_tap_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_IsRightTapEnabled(value)

    @property
    def is_holding_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement].get_IsHoldingEnabled(byref(value))
        return value.value

    @is_holding_enabled.setter
    def is_holding_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement].put_IsHoldingEnabled(value)

    @property
    def manipulation_mode(self) -> enum.Windows.UI.Xaml.Input.ManipulationModes:
        value = enum.Windows.UI.Xaml.Input.ManipulationModes()
        self[interface.Windows.UI.Xaml.IUIElement].get_ManipulationMode(byref(value))
        return value

    @manipulation_mode.setter
    def manipulation_mode(self, value: enum.Windows.UI.Xaml.Input.ManipulationModes):
        self[interface.Windows.UI.Xaml.IUIElement].put_ManipulationMode(value)

    def measure(self, available_size: struct.Windows.Foundation.Size) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IUIElement].Measure(available_size))

    def arrange(self, final_size: struct.Windows.Foundation.Rect) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IUIElement].Arrange(final_size))

    def invalidate_measure(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IUIElement].InvalidateMeasure())

    def invalidate_arrange(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IUIElement].InvalidateArrange())

    def update_layout(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IUIElement].UpdateLayout())

    @property
    def can_drag(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement3].get_CanDrag(byref(value))
        return value.value

    @can_drag.setter
    def can_drag(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement3].put_CanDrag(value)

    @property
    def access_key(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.IUIElement4].get_AccessKey(byref(value))
        return value.value

    @access_key.setter
    def access_key(self, value: str):
        self[interface.Windows.UI.Xaml.IUIElement4].put_AccessKey(HSTRING.from_string(value))

    @property
    def can_be_scroll_anchor(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IUIElement9].get_CanBeScrollAnchor(byref(value))
        return value.value

    @can_be_scroll_anchor.setter
    def can_be_scroll_anchor(self, value: bool):
        self[interface.Windows.UI.Xaml.IUIElement9].put_CanBeScrollAnchor(value)

    @property
    def rotation(self) -> float:
        value = type.FLOAT()
        self[interface.Windows.UI.Xaml.IUIElement5].get_Rotation(byref(value))
        return value.value

    @rotation.setter
    def rotation(self, value: float):
        self[interface.Windows.UI.Xaml.IUIElement5].put_Rotation(value)


class FrameworkElement(UIElement):
    _statics = (interface.Windows.UI.Xaml.IFrameworkElementStatics,
                interface.Windows.UI.Xaml.IFrameworkElementStatics2,
                interface.Windows.UI.Xaml.IFrameworkElementStatics4,
                interface.Windows.UI.Xaml.IFrameworkElementStatics5,
                interface.Windows.UI.Xaml.IFrameworkElementStatics6)
    _interfaces = (interface.Windows.UI.Xaml.IFrameworkElement,
                   interface.Windows.UI.Xaml.IFrameworkElement2,
                   interface.Windows.UI.Xaml.IFrameworkElement3,
                   interface.Windows.UI.Xaml.IFrameworkElement4,
                   interface.Windows.UI.Xaml.IFrameworkElement6,
                   interface.Windows.UI.Xaml.IFrameworkElement7,
                   interface.Windows.UI.Xaml.IFrameworkElementProtected7,
                   interface.Windows.UI.Xaml.IFrameworkElementOverrides,
                   interface.Windows.UI.Xaml.IFrameworkElementOverrides2)

    @classmethod
    @property
    def tag_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_TagProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def language_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_LanguageProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def actual_width_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_ActualWidthProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def actual_height_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_ActualHeightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def width_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_WidthProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def height_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_HeightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def min_width_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MinWidthProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def max_width_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MaxWidthProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def min_height_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MinHeightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def max_height_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MaxHeightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def horizontal_alignment_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_HorizontalAlignmentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def vertical_alignment_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_VerticalAlignmentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def margin_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MarginProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def name_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_NameProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def data_context_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_DataContextProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def style_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_StyleProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def flow_direction_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics].get_FlowDirectionProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def requested_theme_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics2].get_RequestedThemeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_on_interaction_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_AllowFocusOnInteractionProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_margin_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualMarginProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_secondary_thickness_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualSecondaryThicknessProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_primary_thickness_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualPrimaryThicknessProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_secondary_brush_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualSecondaryBrushProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_primary_brush_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualPrimaryBrushProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_when_disabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_AllowFocusWhenDisabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def actual_theme_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.IFrameworkElementStatics6].get_ActualThemeProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def tag(self) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Tag(byref(obj))
        return _Inspectable(obj)

    @tag.setter
    def tag(self, value: _Inspectable):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Tag(value[interface.IInspectable])

    @property
    def language(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Language(byref(value))
        return value.value

    @language.setter
    def language(self, value: str):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Language(HSTRING.from_string(value))

    @property
    def actual_width(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_ActualWidth(byref(value))
        return value.value

    @property
    def actual_height(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_ActualHeight(byref(value))
        return value.value

    @property
    def width(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Width(byref(value))
        return value.value

    @width.setter
    def width(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Width(value)

    @property
    def height(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Height(byref(value))
        return value.value

    @height.setter
    def height(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Height(value)

    @property
    def min_width(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_MinWidth(byref(value))
        return value.value

    @min_width.setter
    def min_width(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_MinWidth(value)

    @property
    def max_width(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_MaxWidth(byref(value))
        return value.value

    @max_width.setter
    def max_width(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_MaxWidth(value)

    @property
    def min_height(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_MinHeight(byref(value))
        return value.value

    @min_height.setter
    def min_height(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_MinHeight(value)

    @property
    def max_height(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_MaxHeight(byref(value))
        return value.value

    @max_height.setter
    def max_height(self, value: float):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_MaxHeight(value)

    @property
    def horizontal_alignment(self) -> enum.Windows.UI.Xaml.HorizontalAlignment:
        value = enum.Windows.UI.Xaml.HorizontalAlignment()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_HorizontalAlignment(byref(value))
        return value

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: enum.Windows.UI.Xaml.HorizontalAlignment):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_HorizontalAlignment(value)

    @property
    def vertical_alignment(self) -> enum.Windows.UI.Xaml.VerticalAlignment:
        value = enum.Windows.UI.Xaml.VerticalAlignment()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_VerticalAlignment(byref(value))
        return value

    @vertical_alignment.setter
    def vertical_alignment(self, value: enum.Windows.UI.Xaml.VerticalAlignment):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_VerticalAlignment(value)

    @property
    def name(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Name(byref(value))
        return value.value

    @name.setter
    def name(self, value: str):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Name(HSTRING.from_string(value))

    @property
    def base_uri(self) -> Uri:
        value = interface.Windows.Foundation.IUriRuntimeClass()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_BaseUri(byref(value))
        return Uri(value)

    @property
    def style(self) -> Style:
        obj = interface.Windows.UI.Xaml.IStyle()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Style(byref(obj))
        return Style(obj)

    @style.setter
    def style(self, value: Style):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_Style(value[interface.Windows.UI.Xaml.IStyle])

    @property
    def parent(self) -> DependencyObject:
        obj = interface.Windows.UI.Xaml.IDependencyObject()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_Parent(byref(obj))
        return DependencyObject(obj)

    @property
    def flow_direction(self) -> enum.Windows.UI.Xaml.FlowDirection:
        value = enum.Windows.UI.Xaml.FlowDirection()
        self[interface.Windows.UI.Xaml.IFrameworkElement].get_FlowDirection(byref(value))
        return value

    @flow_direction.setter
    def flow_direction(self, value: enum.Windows.UI.Xaml.FlowDirection):
        self[interface.Windows.UI.Xaml.IFrameworkElement].put_FlowDirection(value)

    def find_name(self, name: str) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.IFrameworkElement].FindName(HSTRING.from_string(name), byref(obj))
        return _Inspectable(obj)

    @property
    def requested_theme(self) -> enum.Windows.UI.Xaml.ElementTheme:
        value = enum.Windows.UI.Xaml.ElementTheme()
        self[interface.Windows.UI.Xaml.IFrameworkElement2].get_RequestedTheme(byref(value))
        return value

    @requested_theme.setter
    def requested_theme(self, value: enum.Windows.UI.Xaml.ElementTheme):
        self[interface.Windows.UI.Xaml.IFrameworkElement2].put_RequestedTheme(value)

    @property
    def allow_focus_on_interaction(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IFrameworkElement4].get_AllowFocusOnInteraction(byref(value))
        return value.value

    @allow_focus_on_interaction.setter
    def allow_focus_on_interaction(self, value: bool):
        self[interface.Windows.UI.Xaml.IFrameworkElement4].put_AllowFocusOnInteraction(value)

    @property
    def focus_visual_secondary_brush(self) -> Brush:
        obj = interface.Windows.UI.Xaml.Media.IBrush()
        self[interface.Windows.UI.Xaml.IFrameworkElement4].get_FocusVisualSecondaryBrush(byref(obj))
        return Brush(obj)

    @focus_visual_secondary_brush.setter
    def focus_visual_secondary_brush(self, value: Brush):
        self[interface.Windows.UI.Xaml.IFrameworkElement4].put_FocusVisualSecondaryBrush(value[interface.Windows.UI.Xaml.Media.IBrush])

    @property
    def focus_visual_primary_brush(self) -> Brush:
        obj = interface.Windows.UI.Xaml.Media.IBrush()
        self[interface.Windows.UI.Xaml.IFrameworkElement4].get_FocusVisualPrimaryBrush(byref(obj))
        return Brush(obj)

    @focus_visual_primary_brush.setter
    def focus_visual_primary_brush(self, value: Brush):
        self[interface.Windows.UI.Xaml.IFrameworkElement4].put_FocusVisualPrimaryBrush(value[interface.Windows.UI.Xaml.Media.IBrush])

    @property
    def allow_focus_when_disabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IFrameworkElement4].get_AllowFocusWhenDisabled(byref(value))
        return value.value

    @allow_focus_when_disabled.setter
    def allow_focus_when_disabled(self, value: bool):
        self[interface.Windows.UI.Xaml.IFrameworkElement4].put_AllowFocusWhenDisabled(value)

    @property
    def actual_theme(self) -> enum.Windows.UI.Xaml.ElementTheme:
        value = enum.Windows.UI.Xaml.ElementTheme()
        self[interface.Windows.UI.Xaml.IFrameworkElement6].get_ActualTheme(byref(value))
        return value

    @property
    def is_loaded(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IFrameworkElement7].get_IsLoaded(byref(value))
        return value.value


class Control(FrameworkElement):
    _statics = (interface.Windows.UI.Xaml.Controls.IControlFactory,
                interface.Windows.UI.Xaml.Controls.IControlStatics,
                interface.Windows.UI.Xaml.Controls.IControlStatics2,
                interface.Windows.UI.Xaml.Controls.IControlStatics3,
                interface.Windows.UI.Xaml.Controls.IControlStatics4,
                interface.Windows.UI.Xaml.Controls.IControlStatics5,
                interface.Windows.UI.Xaml.Controls.IControlStatics7)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IControl,
                   interface.Windows.UI.Xaml.Controls.IControl2,
                   interface.Windows.UI.Xaml.Controls.IControl3,
                   interface.Windows.UI.Xaml.Controls.IControl4,
                   interface.Windows.UI.Xaml.Controls.IControl5,
                   interface.Windows.UI.Xaml.Controls.IControl7,
                   interface.Windows.UI.Xaml.Controls.IControlProtected,
                   interface.Windows.UI.Xaml.Controls.IControlOverrides,
                   interface.Windows.UI.Xaml.Controls.IControlOverrides6)

    @classmethod
    @property
    def font_size_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontSizeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def font_family_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontFamilyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def font_weight_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontWeightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def font_style_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontStyleProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def font_stretch_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontStretchProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def character_spacing_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_CharacterSpacingProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def foreground_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_ForegroundProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_tab_stop_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_IsTabStopProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_IsEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def tab_index_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_TabIndexProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def tab_navigation_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_TabNavigationProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def template_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_TemplateProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def padding_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_PaddingProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def horizontal_content_alignment_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_HorizontalContentAlignmentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def vertical_content_alignment_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_VerticalContentAlignmentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def background_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_BackgroundProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def border_thickness_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_BorderThicknessProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def border_brush_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_BorderBrushProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def default_style_key_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_DefaultStyleKeyProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def focus_state_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics].get_FocusStateProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_text_scale_factor_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics2].get_IsTextScaleFactorEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def use_system_focus_visuals_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics3].get_UseSystemFocusVisualsProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_template_focus_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics3].get_IsTemplateFocusTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_focus_engagement_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_IsFocusEngagementEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_focus_engaged_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_IsFocusEngagedProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def requires_pointer_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_RequiresPointerProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_left_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusLeftProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_right_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusRightProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_up_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusUpProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_down_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusDownProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def element_sound_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics4].get_ElementSoundModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def default_style_resource_uri_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics5].get_DefaultStyleResourceUriProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_template_key_tip_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics5].get_IsTemplateKeyTipTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def background_sizing_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics7].get_BackgroundSizingProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def corner_radius_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IControlStatics7].get_CornerRadiusProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def font_size(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.Controls.IControl].get_FontSize(byref(value))
        return value.value

    @font_size.setter
    def font_size(self, value: float):
        self[interface.Windows.UI.Xaml.Controls.IControl].put_FontSize(value)

    @property
    def background(self) -> Brush:
        obj = interface.Windows.UI.Xaml.Media.IBrush()
        self[interface.Windows.UI.Xaml.Controls.IControl].get_Background(byref(obj))
        return Brush(obj)

    @background.setter
    def background(self, value: Brush):
        self[interface.Windows.UI.Xaml.Controls.IControl].put_Background(value[interface.Windows.UI.Xaml.Media.IBrush])

    @property
    def background_sizing(self) -> enum.Windows.UI.Xaml.Controls.BackgroundSizing:
        value = enum.Windows.UI.Xaml.Controls.BackgroundSizing()
        self[interface.Windows.UI.Xaml.Controls.IControl7].get_BackgroundSizing(byref(value))
        return value

    @background_sizing.setter
    def background_sizing(self, value: enum.Windows.UI.Xaml.Controls.BackgroundSizing):
        self[interface.Windows.UI.Xaml.Controls.IControl7].put_BackgroundSizing(value)

    @property
    def corner_radius(self) -> struct.Windows.UI.Xaml.CornerRadius:
        value = struct.Windows.UI.Xaml.CornerRadius()
        self[interface.Windows.UI.Xaml.Controls.IControl7].get_CornerRadius(byref(value))
        return value

    @corner_radius.setter
    def corner_radius(self, value: struct.Windows.UI.Xaml.CornerRadius):
        self[interface.Windows.UI.Xaml.Controls.IControl7].put_CornerRadius(value)


class ContentControl(Control):
    _statics = (interface.Windows.UI.Xaml.Controls.IContentControlStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IContentControl,
                   interface.Windows.UI.Xaml.Controls.IContentControl2,
                   interface.Windows.UI.Xaml.Controls.IContentControlOverrides)

    @classmethod
    @property
    def content_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def content_template_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTemplateProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def content_template_selector_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTemplateSelectorProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def content_transitions_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTransitionsProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def content(self) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.Controls.IContentControl].get_Content(byref(obj))
        return _Inspectable(obj)

    @content.setter
    def content(self, value: _Inspectable):
        self[interface.Windows.UI.Xaml.Controls.IContentControl].put_Content(value[interface.IInspectable])


class ButtonBase(ContentControl):
    _statics = (interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IButtonBase,)

    @classmethod
    @property
    def click_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_ClickModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_pointer_over_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_IsPointerOverProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_pressed_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_IsPressedProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def command_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_CommandProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def command_parameter_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_CommandParameterProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def click(self) -> _RoutedEvent:
        return _RoutedEvent(self[interface.Windows.UI.Xaml.Controls.Primitives.IButtonBase], 'Click')

    @click.setter
    def click(self, value: _RoutedEvent):
        pass


class RepeatButton(ButtonBase):
    _statics = (interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButton,)

    @classmethod
    @property
    def delay_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics].get_DelayProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def interval_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButtonStatics].get_IntervalProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def delay(self) -> int:
        value = type.INT32()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButton].get_Delay(byref(value))
        return value.value

    @delay.setter
    def delay(self, value: int):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButton].put_Delay(value)

    @property
    def interval(self) -> int:
        value = type.INT32()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButton].get_Interval(byref(value))
        return value.value

    @interval.setter
    def interval(self, value: int):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IRepeatButton].put_Interval(value)


class _IReference(_Inspectable):
    _t_reference: tuple

    @property
    def value(self):
        obj = self._t_reference[0]()
        self[interface.Windows.Foundation.IReference[self._t_reference[0]]].get_Value(byref(obj))
        return self._t_reference[1](obj)


class ReferenceBoolean(_IReference):
    _t_reference = (type.boolean, bool)
    _interfaces = (interface.Windows.Foundation.IReference[type.boolean],)

    value: bool


class ToggleButton(ButtonBase):
    _statics = (interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonFactory,
                interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics)
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton,
                   interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonOverrides)

    @classmethod
    @property
    def is_checked_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics].get_IsCheckedProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_three_state_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonStatics].get_IsThreeStateProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def is_checked(self) -> ReferenceBoolean:
        obj = interface.Windows.Foundation.IReference[type.boolean]()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton].get_IsChecked(byref(obj))
        return ReferenceBoolean(obj)

    @is_checked.setter
    def is_checked(self, value: ReferenceBoolean):  # TODO
        self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton].put_IsChecked(value[interface.Windows.Foundation.IReference[type.boolean]])

    @property
    def is_three_state(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton].get_IsThreeState(byref(value))
        return value.value

    @is_three_state.setter
    def is_three_state(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton].put_IsThreeState(value)

    @property
    def checked(self) -> _RoutedEvent:
        return _RoutedEvent(self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton], 'Checked')

    @checked.setter
    def checked(self, value: _RoutedEvent):
        pass

    @property
    def unchecked(self) -> _RoutedEvent:
        return _RoutedEvent(self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton], 'Unchecked')

    @unchecked.setter
    def unchecked(self, value: _RoutedEvent):
        pass

    @property
    def indeterminate(self) -> _RoutedEvent:
        return _RoutedEvent(self[interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton], 'Indeterminate')

    @indeterminate.setter
    def indeterminate(self, value: _RoutedEvent):
        pass


class _ButtonWithFlyout(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.Controls.IButtonStaticsWithFlyout,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IButtonWithFlyout,)

    @classmethod
    @property
    def flyout_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IButtonStaticsWithFlyout].get_FlyoutProperty(byref(obj))
        return DependencyProperty(obj)


class Button(_ButtonWithFlyout, ButtonBase):
    _statics = (interface.Windows.UI.Xaml.Controls.IButtonFactory,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IButton,)

    @classmethod
    @property
    def flyout_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IButtonStaticsWithFlyout].get_FlyoutProperty(byref(obj))
        return DependencyProperty(obj)


class DropDownButton(Button):
    _statics = (interface.Windows.UI.Xaml.Controls.IDropDownButtonFactory,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IDropDownButton,)


class Brush(_AnimationObject, DependencyObject):
    _statics = (interface.Windows.UI.Xaml.Media.IBrushStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Media.IBrush,
                   interface.Windows.UI.Xaml.Media.IBrushOverrides2)


class SolidColorBrush(Brush):
    _statics = (interface.Windows.UI.Xaml.Media.ISolidColorBrushFactory,
                interface.Windows.UI.Xaml.Media.ISolidColorBrushStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Media.ISolidColorBrush,)

    @classmethod
    def create_instance_with_color(cls, color: struct.Windows.UI.Color) -> SolidColorBrush:
        obj = interface.Windows.UI.Xaml.Media.ISolidColorBrush()
        cls[interface.Windows.UI.Xaml.Media.ISolidColorBrushFactory].CreateInstanceWithColor(color, byref(obj))
        return SolidColorBrush(obj)

    @classmethod
    @property
    def color_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Media.ISolidColorBrushStatics].get_ColorProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def color(self) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        self[interface.Windows.UI.Xaml.Media.ISolidColorBrush].get_Color(byref(value))
        return value

    @color.setter
    def color(self, value: struct.Windows.UI.Color):
        self[interface.Windows.UI.Xaml.Media.ISolidColorBrush].put_Color(value)


class Panel(FrameworkElement):
    _statics = (interface.Windows.UI.Xaml.Controls.IPanelStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IPanel,
                   interface.Windows.UI.Xaml.Controls.IPanel2)

    @property
    def children(self) -> UIElementCollection:
        obj = interface.Windows.Foundation.Collections.IVector[interface.Windows.UI.Xaml.IUIElement]()
        self[interface.Windows.UI.Xaml.Controls.IPanel].get_Children(byref(obj))
        return UIElementCollection(obj)


class StackPanel(_ScrollSnapPointsInfo, _InsertionPanel, Panel):
    _statics = (interface.Windows.UI.Xaml.Controls.IStackPanelStatics,
                interface.Windows.UI.Xaml.Controls.IStackPanelStatics2,
                interface.Windows.UI.Xaml.Controls.IStackPanelStatics4,
                interface.Windows.UI.Xaml.Controls.IStackPanelStatics5)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IStackPanel,
                   interface.Windows.UI.Xaml.Controls.IStackPanel2,
                   interface.Windows.UI.Xaml.Controls.IStackPanel4,
                   interface.Windows.UI.Xaml.Controls.IStackPanel5)


class TextBlock(FrameworkElement):
    _statics = (interface.Windows.UI.Xaml.Controls.ITextBlockStatics,
                interface.Windows.UI.Xaml.Controls.ITextBlockStatics2,
                interface.Windows.UI.Xaml.Controls.ITextBlockStatics3,
                interface.Windows.UI.Xaml.Controls.ITextBlockStatics5,
                interface.Windows.UI.Xaml.Controls.ITextBlockStatics6,
                interface.Windows.UI.Xaml.Controls.ITextBlockStatics7)
    _interfaces = (interface.Windows.UI.Xaml.Controls.ITextBlock,
                   interface.Windows.UI.Xaml.Controls.ITextBlock2,
                   interface.Windows.UI.Xaml.Controls.ITextBlock3,
                   interface.Windows.UI.Xaml.Controls.ITextBlock4,
                   interface.Windows.UI.Xaml.Controls.ITextBlock5,
                   interface.Windows.UI.Xaml.Controls.ITextBlock6,
                   interface.Windows.UI.Xaml.Controls.ITextBlock7)

    @property
    def font_size(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.Controls.ITextBlock].get_FontSize(byref(value))
        return value.value

    @font_size.setter
    def font_size(self, value: float):
        self[interface.Windows.UI.Xaml.Controls.ITextBlock].put_FontSize(value)

    @property
    def text(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.Controls.ITextBlock].get_Text(byref(value))
        return value.value

    @text.setter
    def text(self, value: str):
        self[interface.Windows.UI.Xaml.Controls.ITextBlock].put_Text(HSTRING.from_string(value))


class PropertyValue(_Inspectable):
    _statics = (interface.Windows.Foundation.IPropertyValueStatics,)
    _interfaces = (interface.Windows.Foundation.IPropertyValue,)

    @classmethod
    def create_empty(cls) -> PropertyValue:
        obj = interface.Windows.Foundation.IPropertyValue()
        cls[interface.Windows.Foundation.IPropertyValueStatics].CreateEmpty(byref(obj))
        return PropertyValue(obj)

    @classmethod
    def create_uint8(cls, value: int) -> PropertyValue:
        obj = interface.Windows.Foundation.IPropertyValue()
        cls[interface.Windows.Foundation.IPropertyValueStatics].CreateUInt8(value, byref(obj))
        return PropertyValue(obj)

    @classmethod
    def create_int16(cls, value: int) -> PropertyValue:
        obj = interface.Windows.Foundation.IPropertyValue()
        cls[interface.Windows.Foundation.IPropertyValueStatics].CreateInt16(value, byref(obj))
        return PropertyValue(obj)

    @classmethod
    def create_boolean(cls, value: bool) -> PropertyValue:
        obj = interface.Windows.Foundation.IPropertyValue()
        cls[interface.Windows.Foundation.IPropertyValueStatics].CreateBoolean(value, byref(obj))
        return PropertyValue(obj)

    @classmethod
    def create_string(cls, value: str) -> PropertyValue:
        obj = interface.IInspectable()
        cls[interface.Windows.Foundation.IPropertyValueStatics].CreateString(HSTRING.from_string(value), byref(obj))
        return PropertyValue(obj)


class Colors(_Inspectable):
    _statics = (interface.Windows.UI.IColorsStatics,)

    @classmethod
    @property
    def alice_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_AliceBlue(byref(value))
        return value

    @classmethod
    @property
    def antique_white(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_AntiqueWhite(byref(value))
        return value

    @classmethod
    @property
    def aqua(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Aqua(byref(value))
        return value

    @classmethod
    @property
    def aquamarine(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Aquamarine(byref(value))
        return value

    @classmethod
    @property
    def azure(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Azure(byref(value))
        return value

    @classmethod
    @property
    def beige(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Beige(byref(value))
        return value

    @classmethod
    @property
    def bisque(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Bisque(byref(value))
        return value

    @classmethod
    @property
    def black(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Black(byref(value))
        return value

    @classmethod
    @property
    def blanched_almond(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_BlanchedAlmond(byref(value))
        return value

    @classmethod
    @property
    def blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Blue(byref(value))
        return value

    @classmethod
    @property
    def blue_violet(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_BlueViolet(byref(value))
        return value

    @classmethod
    @property
    def brown(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Brown(byref(value))
        return value

    @classmethod
    @property
    def burly_wood(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_BurlyWood(byref(value))
        return value

    @classmethod
    @property
    def cadet_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_CadetBlue(byref(value))
        return value

    @classmethod
    @property
    def chartreuse(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Chartreuse(byref(value))
        return value

    @classmethod
    @property
    def chocolate(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Chocolate(byref(value))
        return value

    @classmethod
    @property
    def coral(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Coral(byref(value))
        return value

    @classmethod
    @property
    def cornflower_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_CornflowerBlue(byref(value))
        return value

    @classmethod
    @property
    def cornsilk(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Cornsilk(byref(value))
        return value

    @classmethod
    @property
    def crimson(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Crimson(byref(value))
        return value

    @classmethod
    @property
    def cyan(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Cyan(byref(value))
        return value

    @classmethod
    @property
    def dark_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkBlue(byref(value))
        return value

    @classmethod
    @property
    def dark_cyan(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkCyan(byref(value))
        return value

    @classmethod
    @property
    def dark_goldenrod(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkGoldenrod(byref(value))
        return value

    @classmethod
    @property
    def dark_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkGray(byref(value))
        return value

    @classmethod
    @property
    def dark_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkGreen(byref(value))
        return value

    @classmethod
    @property
    def dark_khaki(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkKhaki(byref(value))
        return value

    @classmethod
    @property
    def dark_magenta(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkMagenta(byref(value))
        return value

    @classmethod
    @property
    def dark_olive_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkOliveGreen(byref(value))
        return value

    @classmethod
    @property
    def dark_orange(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkOrange(byref(value))
        return value

    @classmethod
    @property
    def dark_orchid(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkOrchid(byref(value))
        return value

    @classmethod
    @property
    def dark_red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkRed(byref(value))
        return value

    @classmethod
    @property
    def dark_salmon(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkSalmon(byref(value))
        return value

    @classmethod
    @property
    def dark_sea_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkSeaGreen(byref(value))
        return value

    @classmethod
    @property
    def dark_slate_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkSlateBlue(byref(value))
        return value

    @classmethod
    @property
    def dark_slate_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkSlateGray(byref(value))
        return value

    @classmethod
    @property
    def dark_turquoise(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkTurquoise(byref(value))
        return value

    @classmethod
    @property
    def dark_violet(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DarkViolet(byref(value))
        return value

    @classmethod
    @property
    def deep_pink(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DeepPink(byref(value))
        return value

    @classmethod
    @property
    def deep_sky_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DeepSkyBlue(byref(value))
        return value

    @classmethod
    @property
    def dim_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DimGray(byref(value))
        return value

    @classmethod
    @property
    def dodger_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_DodgerBlue(byref(value))
        return value

    @classmethod
    @property
    def firebrick(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Firebrick(byref(value))
        return value

    @classmethod
    @property
    def floral_white(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_FloralWhite(byref(value))
        return value

    @classmethod
    @property
    def forest_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_ForestGreen(byref(value))
        return value

    @classmethod
    @property
    def fuchsia(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Fuchsia(byref(value))
        return value

    @classmethod
    @property
    def gainsboro(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Gainsboro(byref(value))
        return value

    @classmethod
    @property
    def ghost_white(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_GhostWhite(byref(value))
        return value

    @classmethod
    @property
    def gold(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Gold(byref(value))
        return value

    @classmethod
    @property
    def goldenrod(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Goldenrod(byref(value))
        return value

    @classmethod
    @property
    def gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Gray(byref(value))
        return value

    @classmethod
    @property
    def green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Green(byref(value))
        return value

    @classmethod
    @property
    def green_yellow(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_GreenYellow(byref(value))
        return value

    @classmethod
    @property
    def honeydew(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Honeydew(byref(value))
        return value

    @classmethod
    @property
    def hot_pink(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_HotPink(byref(value))
        return value

    @classmethod
    @property
    def indian_red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_IndianRed(byref(value))
        return value

    @classmethod
    @property
    def indigo(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Indigo(byref(value))
        return value

    @classmethod
    @property
    def ivory(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Ivory(byref(value))
        return value

    @classmethod
    @property
    def khaki(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Khaki(byref(value))
        return value

    @classmethod
    @property
    def lavender(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Lavender(byref(value))
        return value

    @classmethod
    @property
    def lavender_blush(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LavenderBlush(byref(value))
        return value

    @classmethod
    @property
    def lawn_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LawnGreen(byref(value))
        return value

    @classmethod
    @property
    def lemon_chiffon(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LemonChiffon(byref(value))
        return value

    @classmethod
    @property
    def light_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightBlue(byref(value))
        return value

    @classmethod
    @property
    def light_coral(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightCoral(byref(value))
        return value

    @classmethod
    @property
    def light_cyan(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightCyan(byref(value))
        return value

    @classmethod
    @property
    def light_goldenrod_yellow(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightGoldenrodYellow(byref(value))
        return value

    @classmethod
    @property
    def light_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightGreen(byref(value))
        return value

    @classmethod
    @property
    def light_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightGray(byref(value))
        return value

    @classmethod
    @property
    def light_pink(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightPink(byref(value))
        return value

    @classmethod
    @property
    def light_salmon(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightSalmon(byref(value))
        return value

    @classmethod
    @property
    def light_sea_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightSeaGreen(byref(value))
        return value

    @classmethod
    @property
    def light_sky_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightSkyBlue(byref(value))
        return value

    @classmethod
    @property
    def light_slate_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightSlateGray(byref(value))
        return value

    @classmethod
    @property
    def light_steel_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightSteelBlue(byref(value))
        return value

    @classmethod
    @property
    def light_yellow(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LightYellow(byref(value))
        return value

    @classmethod
    @property
    def lime(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Lime(byref(value))
        return value

    @classmethod
    @property
    def lime_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_LimeGreen(byref(value))
        return value

    @classmethod
    @property
    def linen(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Linen(byref(value))
        return value

    @classmethod
    @property
    def magenta(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Magenta(byref(value))
        return value

    @classmethod
    @property
    def maroon(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Maroon(byref(value))
        return value

    @classmethod
    @property
    def medium_aquamarine(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumAquamarine(byref(value))
        return value

    @classmethod
    @property
    def medium_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumBlue(byref(value))
        return value

    @classmethod
    @property
    def medium_orchid(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumOrchid(byref(value))
        return value

    @classmethod
    @property
    def medium_purple(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumPurple(byref(value))
        return value

    @classmethod
    @property
    def medium_sea_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumSeaGreen(byref(value))
        return value

    @classmethod
    @property
    def medium_slate_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumSlateBlue(byref(value))
        return value

    @classmethod
    @property
    def medium_spring_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumSpringGreen(byref(value))
        return value

    @classmethod
    @property
    def medium_turquoise(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumTurquoise(byref(value))
        return value

    @classmethod
    @property
    def medium_violet_red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MediumVioletRed(byref(value))
        return value

    @classmethod
    @property
    def midnight_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MidnightBlue(byref(value))
        return value

    @classmethod
    @property
    def mint_cream(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MintCream(byref(value))
        return value

    @classmethod
    @property
    def misty_rose(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_MistyRose(byref(value))
        return value

    @classmethod
    @property
    def moccasin(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Moccasin(byref(value))
        return value

    @classmethod
    @property
    def navajo_white(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_NavajoWhite(byref(value))
        return value

    @classmethod
    @property
    def navy(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Navy(byref(value))
        return value

    @classmethod
    @property
    def old_lace(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_OldLace(byref(value))
        return value

    @classmethod
    @property
    def olive(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Olive(byref(value))
        return value

    @classmethod
    @property
    def olive_drab(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_OliveDrab(byref(value))
        return value

    @classmethod
    @property
    def orange(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Orange(byref(value))
        return value

    @classmethod
    @property
    def orange_red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_OrangeRed(byref(value))
        return value

    @classmethod
    @property
    def orchid(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Orchid(byref(value))
        return value

    @classmethod
    @property
    def pale_goldenrod(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PaleGoldenrod(byref(value))
        return value

    @classmethod
    @property
    def pale_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PaleGreen(byref(value))
        return value

    @classmethod
    @property
    def pale_turquoise(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PaleTurquoise(byref(value))
        return value

    @classmethod
    @property
    def pale_violet_red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PaleVioletRed(byref(value))
        return value

    @classmethod
    @property
    def papaya_whip(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PapayaWhip(byref(value))
        return value

    @classmethod
    @property
    def peach_puff(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PeachPuff(byref(value))
        return value

    @classmethod
    @property
    def peru(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Peru(byref(value))
        return value

    @classmethod
    @property
    def pink(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Pink(byref(value))
        return value

    @classmethod
    @property
    def plum(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Plum(byref(value))
        return value

    @classmethod
    @property
    def powder_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_PowderBlue(byref(value))
        return value

    @classmethod
    @property
    def purple(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Purple(byref(value))
        return value

    @classmethod
    @property
    def red(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Red(byref(value))
        return value

    @classmethod
    @property
    def rosy_brown(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_RosyBrown(byref(value))
        return value

    @classmethod
    @property
    def royal_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_RoyalBlue(byref(value))
        return value

    @classmethod
    @property
    def saddle_brown(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SaddleBrown(byref(value))
        return value

    @classmethod
    @property
    def salmon(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Salmon(byref(value))
        return value

    @classmethod
    @property
    def sandy_brown(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SandyBrown(byref(value))
        return value

    @classmethod
    @property
    def sea_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SeaGreen(byref(value))
        return value

    @classmethod
    @property
    def sea_shell(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SeaShell(byref(value))
        return value

    @classmethod
    @property
    def sienna(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Sienna(byref(value))
        return value

    @classmethod
    @property
    def silver(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Silver(byref(value))
        return value

    @classmethod
    @property
    def sky_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SkyBlue(byref(value))
        return value

    @classmethod
    @property
    def slate_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SlateBlue(byref(value))
        return value

    @classmethod
    @property
    def slate_gray(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SlateGray(byref(value))
        return value

    @classmethod
    @property
    def snow(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Snow(byref(value))
        return value

    @classmethod
    @property
    def spring_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SpringGreen(byref(value))
        return value

    @classmethod
    @property
    def steel_blue(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_SteelBlue(byref(value))
        return value

    @classmethod
    @property
    def tan(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Tan(byref(value))
        return value

    @classmethod
    @property
    def teal(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Teal(byref(value))
        return value

    @classmethod
    @property
    def thistle(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Thistle(byref(value))
        return value

    @classmethod
    @property
    def tomato(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Tomato(byref(value))
        return value

    @classmethod
    @property
    def transparent(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Transparent(byref(value))
        return value

    @classmethod
    @property
    def turquoise(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Turquoise(byref(value))
        return value

    @classmethod
    @property
    def violet(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Violet(byref(value))
        return value

    @classmethod
    @property
    def wheat(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Wheat(byref(value))
        return value

    @classmethod
    @property
    def white(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_White(byref(value))
        return value

    @classmethod
    @property
    def white_smoke(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_WhiteSmoke(byref(value))
        return value

    @classmethod
    @property
    def yellow(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_Yellow(byref(value))
        return value

    @classmethod
    @property
    def yellow_green(cls) -> struct.Windows.UI.Color:
        value = struct.Windows.UI.Color()
        cls[interface.Windows.UI.IColorsStatics].get_YellowGreen(byref(value))
        return value


class XamlReader(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.Markup.IXamlReaderStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Markup.IXamlReader,)

    @classmethod
    def load(cls, xaml: str) -> _Inspectable:
        obj = interface.IInspectable()
        cls[interface.Windows.UI.Xaml.Markup.IXamlReaderStatics].Load(HSTRING.from_string(xaml), byref(obj))
        return _Inspectable(obj)

    @classmethod
    def load_with_initial_template_validation(cls, xaml: str) -> _Inspectable:
        obj = interface.IInspectable()
        cls[interface.Windows.UI.Xaml.Markup.IXamlReaderStatics].LoadWithInitialTemplateValidation(HSTRING.from_string(xaml), byref(obj))
        return _Inspectable(obj)


class SetterBase(DependencyObject):
    _statics = (interface.Windows.UI.Xaml.ISetterBaseFactory,)
    _interfaces = (interface.Windows.UI.Xaml.ISetterBase,)

    @property
    def is_sealed(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.ISetterBase].get_IsSealed(byref(value))
        return value.value


class _IIterator(_Inspectable):
    _t_iterator: tuple[builtins.type[interface.IInspectable], Optional[builtins.type[_Inspectable]]]

    @property
    def current(self):
        obj = self._t_iterator[0]()
        self[interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].get_Current(byref(obj))
        return obj if self._t_iterator[1] is None else self._t_iterator[1](obj)

    @property
    def has_current(self) -> bool:
        value = boolean()
        self[interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].get_HasCurrent(byref(value))
        return value.value

    def move_next(self) -> bool:
        value = boolean()
        self[interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].MoveNext(byref(value))
        return value.value


class IteratorSetterBase(_IIterator):
    _t_iterator = interface.Windows.UI.Xaml.ISetterBase, SetterBase
    _interfaces = (interface.Windows.Foundation.Collections.IIterator[interface.Windows.UI.Xaml.ISetterBase],)

    current: SetterBase


class _IIterable(_Inspectable):
    _t_iterable: tuple[builtins.type[interface.IInspectable], Optional[builtins.type[_Inspectable]]]

    def first(self):
        obj = interface.Windows.Foundation.Collections.IIterator[self._t_iterable[0]]()
        self[interface.Windows.Foundation.Collections.IIterable[self._t_iterable[0]]].First(byref(obj))
        return obj if self._t_iterable[1] is None else self._t_iterable[1](obj)


class IterableSetterBase(_IIterable):
    _t_iterable = interface.Windows.UI.Xaml.ISetterBase, IteratorSetterBase
    _interfaces = (interface.Windows.Foundation.Collections.IIterable[interface.Windows.UI.Xaml.ISetterBase],)

    first: Callable[[], IteratorSetterBase]


class _IVector(_Inspectable):
    _t_vector: tuple[builtins.type[interface.IInspectable], Optional[builtins.type[_Inspectable]]]

    def get_at(self, index: int):
        obj = self._t_vector[0]()
        self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].GetAt(index, byref(obj))
        return obj if self._t_vector[1] is None else self._t_vector[1](obj)

    @property
    def size(self) -> int:
        value = type.c_uint()
        self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].get_Size(byref(value))
        return value.value

    def set_at(self, index: int, value) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].SetAt(index, value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def insert_at(self, index: int, value) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].InsertAt(index, value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def remove_at(self, index: int) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].RemoveAt(index))

    def append(self, value) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].Append(value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def remove_at_end(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].RemoveAtEnd())

    def clear(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].Clear())


class _IKeyValuePair(_Inspectable):
    _k_key_value_pair: tuple
    _v_key_value_pair: tuple

    @property
    def key(self):
        obj = self._k_key_value_pair[0]()
        self[interface.Windows.Foundation.Collections.IKeyValuePair[self._k_key_value_pair[0], self._v_key_value_pair[0]]].get_Key(byref(obj))
        return obj if self._k_key_value_pair[1] is None else self._k_key_value_pair[1](obj)

    @property
    def value(self):
        obj = self._v_key_value_pair[0]()
        self[interface.Windows.Foundation.Collections.IKeyValuePair[self._k_key_value_pair[0], self._v_key_value_pair[0]]].get_Value(byref(obj))
        return obj if self._v_key_value_pair[1] is None else self._v_key_value_pair[1](obj)


class KeyValuePairHSTRINGHSTRING(_IKeyValuePair):
    _k_key_value_pair = HSTRING, str
    _v_key_value_pair = HSTRING, str
    _interfaces = (interface.Windows.Foundation.Collections.IKeyValuePair[HSTRING, HSTRING],)

    key: str
    value: str


class _IMap(_Inspectable):
    _k_map: tuple
    _v_map: tuple

    def lookup(self, key):
        obj = self._v_map[0]()
        self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].Lookup(key if self._k_map[1] is None else key[self._k_map[0]], byref(obj))
        return obj if self._v_map[1] is None else self._v_map[1](obj)

    @property
    def size(self) -> int:
        value = type.c_uint()
        self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].get_Size(byref(value))
        return value.value

    def has_key(self, key) -> bool:
        found = boolean()
        self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].HasKey(key if self._k_map[1] is None else key[self._k_map[0]], byref(found))
        return found.value

    def insert(self, key, value) -> bool:
        replaced = boolean()
        self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].Insert(key if self._k_map[1] is None else key[self._k_map[0]], value if self._v_map[1] is None else value[self._v_map[0]], byref(replaced))
        return replaced.value

    def remove(self, key) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].Remove(key if self._k_map[1] is None else key[self._k_map[0]]))

    def clear(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Foundation.Collections.IMap[self._k_map[0], self._v_map[0]]].Clear())


class MapHSTRINGHSTRING(_IMap):
    _k_map = HSTRING, str
    _v_map = HSTRING, str
    _interfaces = (interface.Windows.Foundation.Collections.IMap[HSTRING, HSTRING],)

    has_key: Callable[[str], bool]
    insert: Callable[[str, str], bool]
    remove: Callable[[str], bool]
    clear: Callable[[], bool]


class DependencyProperty(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.IDependencyPropertyStatics,)
    _interfaces = (interface.Windows.UI.Xaml.IDependencyProperty,)

    @classmethod
    def unset_value(cls) -> _Inspectable:
        obj = interface.IInspectable()
        cls[interface.Windows.UI.Xaml.IDependencyPropertyStatics].get_UnsetValue(byref(obj))
        return _Inspectable(obj)

    def get_metadata(self, for_type: struct.Windows.UI.Xaml.Interop.TypeName) -> PropertyMetadata:
        obj = interface.Windows.UI.Xaml.IPropertyMetadata()
        self[interface.Windows.UI.Xaml.IDependencyProperty].GetMetadata(for_type, byref(obj))
        return PropertyMetadata(obj)


class Setter(SetterBase):
    _statics = (interface.Windows.UI.Xaml.ISetterFactory,)
    _interfaces = (interface.Windows.UI.Xaml.ISetter,
                   interface.Windows.UI.Xaml.ISetter2,)

    @classmethod
    def create_instance(cls, target_property: DependencyProperty, value: _Inspectable) -> Setter:
        obj = interface.Windows.UI.Xaml.ISetter()
        cls[interface.Windows.UI.Xaml.ISetterFactory].CreateInstance(target_property[interface.Windows.UI.Xaml.IDependencyProperty], value[interface.IInspectable], byref(obj))
        return Setter(obj)

    @property
    def property(self) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        self[interface.Windows.UI.Xaml.ISetter].get_Property(byref(obj))
        return DependencyProperty(obj)

    @property.setter
    def property(self, value: DependencyProperty):
        self[interface.Windows.UI.Xaml.ISetter].put_Property(value[interface.Windows.UI.Xaml.IDependencyProperty])

    @builtins.property
    def value(self) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.ISetter].get_Value(byref(obj))
        return _Inspectable(obj)

    # noinspection PyUnresolvedReferences
    @value.setter
    def value(self, value: _Inspectable):
        self[interface.Windows.UI.Xaml.ISetter].put_Value(value[interface.IInspectable])


class MenuFlyoutItemBase(Control):
    _statics = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBaseFactory,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase,)


class VectorUIElement(_IVector):
    _t_vector = interface.Windows.UI.Xaml.IUIElement, UIElement
    _interfaces = (interface.Windows.Foundation.Collections.IVector[interface.Windows.UI.Xaml.IUIElement],)

    get_at: Callable[[int], UIElement]
    set_at: Callable[[int, UIElement], bool]
    insert_at: Callable[[int, UIElement], bool]
    append: Callable[[UIElement], bool]


class VectorSetterBase(_IVector):
    _t_vector = interface.Windows.UI.Xaml.ISetterBase, SetterBase
    _interfaces = (interface.Windows.Foundation.Collections.IVector[interface.Windows.UI.Xaml.ISetterBase],)

    get_at: Callable[[int], SetterBase]
    set_at: Callable[[int, SetterBase], bool]
    insert_at: Callable[[int, SetterBase], bool]
    append: Callable[[SetterBase], bool]


class VectorMenuFlyoutItemBase(_IVector):
    _t_vector = interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase, MenuFlyoutItemBase
    _interfaces = (interface.Windows.Foundation.Collections.IVector[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase],)

    get_at: Callable[[int], MenuFlyoutItemBase]
    set_at: Callable[[int, MenuFlyoutItemBase], bool]
    insert_at: Callable[[int, MenuFlyoutItemBase], bool]
    append: Callable[[MenuFlyoutItemBase], bool]


class UIElementCollection(VectorUIElement):
    _interfaces = (interface.Windows.UI.Xaml.Controls.IUIElementCollection,)


class SetterBaseCollection(IterableSetterBase, VectorSetterBase):
    _interfaces = (interface.Windows.UI.Xaml.ISetterBaseCollection,)

    @property
    def is_sealed(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.ISetterBase].get_IsSealed(byref(value))
        return value.value


class FlyoutBase(DependencyObject):
    _statics = (interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics,
                interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2,
                interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3,
                interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5,
                interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6)
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase4,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides,
                   interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides4)

    @classmethod
    @property
    def placement_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].get_PlacementProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def attached_flyout_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].get_AttachedFlyoutProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    def get_attached_flyout(cls, element: FrameworkElement) -> FlyoutBase:
        obj = interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].GetAttachedFlyout(element[interface.Windows.UI.Xaml.IFrameworkElement], byref(obj))
        return FlyoutBase(obj)

    @classmethod
    def set_attached_flyout(cls, element: FrameworkElement, value: FlyoutBase) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].SetAttachedFlyout(
            element[interface.Windows.UI.Xaml.IFrameworkElement], value[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase]))

    @classmethod
    def show_attached_flyout(cls, element: FrameworkElement) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].ShowAttachedFlyout(element[interface.Windows.UI.Xaml.IFrameworkElement]))

    @classmethod
    @property
    def allow_focus_on_interaction_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_AllowFocusOnInteractionProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def light_dismiss_overlay_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_LightDismissOverlayModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_when_disabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_AllowFocusWhenDisabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def element_sound_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_ElementSoundModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def overlay_input_pass_through_element_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3].get_OverlayInputPassThroughElementProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_TargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def show_mode_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_ShowModeProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def input_device_prefers_primary_commands_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_InputDevicePrefersPrimaryCommandsProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def are_open_close_animations_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_AreOpenCloseAnimationsEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_open_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_IsOpenProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def should_constrain_to_root_bounds_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6].get_ShouldConstrainToRootBoundsProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def placement(self) -> enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].get_Placement(byref(value))
        return value

    @placement.setter
    def placement(self, value: enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].put_Placement(value)

    def show_at(self, placement_target: FrameworkElement) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].ShowAt(placement_target[interface.Windows.UI.Xaml.IFrameworkElement]))

    def hide(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].Hide())

    @property
    def target(self) -> FrameworkElement:
        obj = interface.Windows.UI.Xaml.IFrameworkElement()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_Target(byref(obj))
        return FrameworkElement(obj)

    @property
    def allow_focus_on_interaction(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_AllowFocusOnInteraction(byref(value))
        return value.value

    @allow_focus_on_interaction.setter
    def allow_focus_on_interaction(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_AllowFocusOnInteraction(value)

    @property
    def light_dismiss_overlay_mode(self) -> enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode:
        value = enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_LightDismissOverlayMode(byref(value))
        return value

    @light_dismiss_overlay_mode.setter
    def light_dismiss_overlay_mode(self, value: enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_LightDismissOverlayMode(value)

    @property
    def allow_focus_when_disabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_AllowFocusWhenDisabled(byref(value))
        return value.value

    @allow_focus_when_disabled.setter
    def allow_focus_when_disabled(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_AllowFocusWhenDisabled(value)

    @property
    def element_sound_mode(self) -> enum.Windows.UI.Xaml.ElementSoundMode:
        value = enum.Windows.UI.Xaml.ElementSoundMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_ElementSoundMode(byref(value))
        return value

    @element_sound_mode.setter
    def element_sound_mode(self, value: enum.Windows.UI.Xaml.ElementSoundMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_ElementSoundMode(value)

    @property
    def overlay_input_pass_through_element(self) -> DependencyObject:
        obj = interface.Windows.UI.Xaml.IDependencyObject()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3].get_OverlayInputPassThroughElement(byref(obj))
        return DependencyObject(obj)

    @overlay_input_pass_through_element.setter
    def overlay_input_pass_through_element(self, value: DependencyObject):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3].put_OverlayInputPassThroughElement(value[interface.Windows.UI.Xaml.IDependencyObject])

    @property
    def show_mode(self) -> enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_ShowMode(byref(value))
        return value

    @show_mode.setter
    def show_mode(self, value: enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].put_ShowMode(value)

    @property
    def input_device_prefers_primary_commands(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_InputDevicePrefersPrimaryCommands(byref(value))
        return value.value

    @property
    def are_open_close_animations_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_AreOpenCloseAnimationsEnabled(byref(value))
        return value.value

    @are_open_close_animations_enabled.setter
    def are_open_close_animations_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].put_AreOpenCloseAnimationsEnabled(value)

    @property
    def is_open(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_IsOpen(byref(value))
        return value.value

    def show_at_(self, placement_target: DependencyObject, show_options: FlyoutShowOptions) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].ShowAt(
            placement_target[interface.Windows.UI.Xaml.IDependencyObject], show_options[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions]))

    @property
    def should_constrain_to_root_bounds(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].get_ShouldConstrainToRootBounds(byref(value))
        return value.value

    @should_constrain_to_root_bounds.setter
    def should_constrain_to_root_bounds(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].put_ShouldConstrainToRootBounds(value)

    @property
    def is_constrained_to_root_bounds(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].get_IsConstrainedToRootBounds(byref(value))
        return value.value


class FlyoutShowOptions(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions,)

    @property
    def show_mode(self) -> enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].get_ShowMode(byref(value))
        return value

    @show_mode.setter
    def show_mode(self, value: enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].put_ShowMode(value)

    @property
    def placement(self) -> enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode()
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].get_Placement(byref(value))
        return value

    @placement.setter
    def placement(self, value: enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode):
        self[interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].put_Placement(value)


class _ItemContainerMapping(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.Controls.IItemContainerMapping,)


class ItemsControl(_ItemContainerMapping, Control):
    _statics = (interface.Windows.UI.Xaml.Controls.IItemsControlFactory,
                interface.Windows.UI.Xaml.Controls.IItemsControlStatics)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IItemsControl,
                   interface.Windows.UI.Xaml.Controls.IItemsControl2,
                   interface.Windows.UI.Xaml.Controls.IItemsControl3,
                   interface.Windows.UI.Xaml.Controls.IItemsControlOverrides)

    @classmethod
    @property
    def items_source_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemsSourceProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def item_template_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemTemplateProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def item_template_selector_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemTemplateSelectorProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def items_panel_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemsPanelProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def display_member_path_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_DisplayMemberPathProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_style_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerStyleProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_style_selector_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerStyleSelectorProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_transitions_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerTransitionsProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def group_style_selector_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_GroupStyleSelectorProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_grouping_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_IsGroupingProperty(byref(obj))
        return DependencyProperty(obj)


class MenuFlyoutPresenter(ItemsControl):
    _statics = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterFactory,
                interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterStatics3)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter,
                   interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter2,
                   interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3)

    @classmethod
    @property
    def is_default_shadow_enabled_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterStatics3].get_IsDefaultShadowEnabledProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def is_default_shadow_enabled(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3].get_IsDefaultShadowEnabled(byref(value))
        return value.value

    @is_default_shadow_enabled.setter
    def is_default_shadow_enabled(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3].put_IsDefaultShadowEnabled(value)


class MenuFlyout(FlyoutBase):
    _statics = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IMenuFlyout,
                   interface.Windows.UI.Xaml.Controls.IMenuFlyout2)

    @property
    def items(self) -> VectorMenuFlyoutItemBase:
        obj = interface.Windows.Foundation.Collections.IVector[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase]()
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyout].get_Items(byref(obj))
        return VectorMenuFlyoutItemBase(obj)

    @property
    def menu_flyout_presenter_style(self) -> Style:
        obj = interface.Windows.UI.Xaml.IStyle()
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyout].get_MenuFlyoutPresenterStyle(byref(obj))
        return Style(obj)

    @menu_flyout_presenter_style.setter
    def menu_flyout_presenter_style(self, value: Style):
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyout].put_MenuFlyoutPresenterStyle(value[interface.Windows.UI.Xaml.IStyle])

    def show_at__(self, target_element: UIElement, point: struct.Windows.Foundation.Point) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.Controls.IMenuFlyout2].ShowAt(target_element[interface.Windows.UI.Xaml.IUIElement], point))


class MenuFlyoutItem(MenuFlyoutItemBase):
    _statics = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemFactory,
                interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics,
                interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics2,
                interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics3)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem,
                   interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem2,
                   interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3)

    @classmethod
    @property
    def text_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_TextProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def command_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_CommandProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def command_parameter_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_CommandParameterProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def icon_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics2].get_IconProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_text_override_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics3].get_KeyboardAcceleratorTextOverrideProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def text(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem].get_Text(byref(value))
        return value.value

    @text.setter
    def text(self, value: str):
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem].put_Text(HSTRING.from_string(value))

    @property
    def keyboard_accelerator_text_override(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3].get_KeyboardAcceleratorTextOverride(byref(value))
        return value.value

    @keyboard_accelerator_text_override.setter
    def keyboard_accelerator_text_override(self, value: str):
        self[interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3].put_KeyboardAcceleratorTextOverride(HSTRING.from_string(value))


class Style(DependencyObject):
    _statics = (interface.Windows.UI.Xaml.IStyleFactory,)
    _interfaces = (interface.Windows.UI.Xaml.IStyle,)

    @classmethod
    def create_instance(cls, target_type: struct.Windows.UI.Xaml.Interop.TypeName) -> Style:
        obj = interface.Windows.UI.Xaml.IStyle()
        cls[interface.Windows.UI.Xaml.IStyleFactory].CreateInstance(target_type, byref(obj))
        return Style(obj)

    @property
    def is_sealed(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.IStyle].get_IsSealed(byref(value))
        return value.value

    @property
    def setters(self) -> SetterBaseCollection:
        obj = interface.Windows.UI.Xaml.ISetterBaseCollection()
        self[interface.Windows.UI.Xaml.IStyle].get_Setters(byref(obj))
        return SetterBaseCollection(obj)

    @property
    def target_type(self) -> struct.Windows.UI.Xaml.Interop.TypeName:
        value = struct.Windows.UI.Xaml.Interop.TypeName()
        self[interface.Windows.UI.Xaml.IStyle].get_TargetType(byref(value))
        return value

    @target_type.setter
    def target_type(self, value: struct.Windows.UI.Xaml.Interop.TypeName):
        self[interface.Windows.UI.Xaml.IStyle].put_TargetType(value)

    @property
    def based_on(self) -> Style:
        obj = interface.Windows.UI.Xaml.IStyle()
        self[interface.Windows.UI.Xaml.IStyle].get_BasedOn(byref(obj))
        return Style(obj)

    @based_on.setter
    def based_on(self, value: Style):
        self[interface.Windows.UI.Xaml.IStyle].put_BasedOn(value[interface.Windows.UI.Xaml.IStyle])

    def seal(self) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Xaml.IStyle].Seal())


class PropertyMetadata(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.IPropertyMetadataFactory,
                interface.Windows.UI.Xaml.IPropertyMetadataStatics)
    _interfaces = (interface.Windows.UI.Xaml.IPropertyMetadata,)

    @property
    def default_value(self) -> _Inspectable:
        obj = interface.IInspectable()
        self[interface.Windows.UI.Xaml.IPropertyMetadata].get_DefaultValue(byref(obj))
        return _Inspectable(obj)


class _Stringable(_Inspectable):
    _interfaces = (interface.Windows.Foundation.IStringable,)

    def to_string(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IStringable].ToString(byref(value))
        return value.value


class _UriRuntimeClassWithAbsoluteCanonicalUri(_Inspectable):
    _interfaces = (interface.Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri,)

    @property
    def absolute_canonical_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri].get_AbsoluteCanonicalUri(byref(value))
        return value.value

    @property
    def display_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri].get_DisplayUri(byref(value))
        return value.value


class WwwFormUrlDecoder(_Inspectable):
    _statics = (interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClassFactory,)
    _interfaces = (interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass,)

    @classmethod
    def create_www_form_url_decoder(cls, query: str) -> WwwFormUrlDecoder:
        obj = interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass()
        cls[interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClassFactory].CreateWwwFormUrlDecoder(HSTRING.from_string(query), byref(obj))
        return WwwFormUrlDecoder(obj)

    def get_first_value_by_name(self, name: str) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass].GetFirstValueByName(HSTRING.from_string(name), byref(value))
        return value.value


class Uri(_UriRuntimeClassWithAbsoluteCanonicalUri, _Stringable):
    _statics = (interface.Windows.Foundation.IUriRuntimeClassFactory,)
    _interfaces = (interface.Windows.Foundation.IUriRuntimeClass,)

    @classmethod
    def create_uri(cls, uri: str) -> Uri:
        obj = interface.Windows.Foundation.IUriRuntimeClass()
        cls[interface.Windows.Foundation.IUriRuntimeClassFactory].CreateUri(HSTRING.from_string(uri), byref(obj))
        return Uri(obj)

    @classmethod
    def create_with_relative_uri(cls, base_uri: str, relative_uri: str) -> Uri:
        obj = interface.Windows.Foundation.IUriRuntimeClass()
        cls[interface.Windows.Foundation.IUriRuntimeClassFactory].CreateWithRelativeUri(HSTRING.from_string(base_uri), HSTRING.from_string(relative_uri), byref(obj))
        return Uri(obj)

    @property
    def absolute_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_AbsoluteUri(byref(value))
        return value.value

    @property
    def display_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_DisplayUri(byref(value))
        return value.value

    @property
    def domain(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Domain(byref(value))
        return value.value

    @property
    def extension(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Extension(byref(value))
        return value.value

    @property
    def fragment(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Fragment(byref(value))
        return value.value

    @property
    def host(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Host(byref(value))
        return value.value

    @property
    def password(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Password(byref(value))
        return value.value

    @property
    def path(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Path(byref(value))
        return value.value

    @property
    def query(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Query(byref(value))
        return value.value

    @property
    def query_parsed(self) -> WwwFormUrlDecoder:
        obj = interface.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_QueryParsed(byref(obj))
        return WwwFormUrlDecoder(obj)

    @property
    def raw_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_RawUri(byref(value))
        return value.value

    @property
    def scheme_name(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_SchemeName(byref(value))
        return value.value

    @property
    def user_name(self) -> str:
        value = HSTRING()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_UserName(byref(value))
        return value.value

    @property
    def port(self) -> int:
        value = type.INT32()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Port(byref(value))
        return value.value

    @property
    def suspicious(self) -> bool:
        value = boolean()
        self[interface.Windows.Foundation.IUriRuntimeClass].get_Suspicious(byref(value))
        return value.value

    def equals(self, uri: Uri) -> bool:
        value = boolean()
        self[interface.Windows.Foundation.IUriRuntimeClass].Equals(uri[interface.Windows.Foundation.IUriRuntimeClass], byref(value))
        return value.value

    def combine_uri(self, relative_uri: str) -> Uri:
        obj = interface.Windows.Foundation.IUriRuntimeClass()
        self[interface.Windows.Foundation.IUriRuntimeClass].CombineUri(HSTRING.from_string(relative_uri), byref(obj))
        return Uri(obj)


class HyperlinkButton(ButtonBase):
    _statics = (interface.Windows.UI.Xaml.Controls.IHyperlinkButtonFactory,
                interface.Windows.UI.Xaml.Controls.IHyperlinkButtonStatics)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IHyperlinkButton,)

    @classmethod
    @property
    def navigate_uri_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IHyperlinkButtonStatics].get_NavigateUriProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def navigate_uri(self) -> Uri:
        obj = interface.Windows.Foundation.IUriRuntimeClass()
        self[interface.Windows.UI.Xaml.Controls.IHyperlinkButton].get_NavigateUri(byref(obj))
        return Uri(obj)

    @navigate_uri.setter
    def navigate_uri(self, value: Uri):
        self[interface.Windows.UI.Xaml.Controls.IHyperlinkButton].put_NavigateUri(value[interface.Windows.Foundation.IUriRuntimeClass])


class IconElement(FrameworkElement):
    _statics = (interface.Windows.UI.Xaml.Controls.IIconElementFactory,
                interface.Windows.UI.Xaml.Controls.IIconElementStatics)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IIconElement,)

    @classmethod
    @property
    def foreground_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IIconElementStatics].get_ForegroundProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def foreground(self) -> Brush:
        obj = interface.Windows.UI.Xaml.Media.IBrush()
        self[interface.Windows.UI.Xaml.Controls.IIconElement].get_Foreground(byref(obj))
        return Brush(obj)

    @foreground.setter
    def foreground(self, value: Brush):
        self[interface.Windows.UI.Xaml.Controls.IIconElement].put_Foreground(value[interface.Windows.UI.Xaml.Media.IBrush])


class SymbolIcon(IconElement):
    _statics = (interface.Windows.UI.Xaml.Controls.ISymbolIconFactory,
                interface.Windows.UI.Xaml.Controls.ISymbolIconStatics)
    _interfaces = (interface.Windows.UI.Xaml.Controls.ISymbolIcon,)

    @classmethod
    def create_instance_with_symbol(cls, symbol: enum.Windows.UI.Xaml.Controls.Symbol) -> SymbolIcon:
        obj = interface.Windows.UI.Xaml.Controls.ISymbolIcon()
        cls[interface.Windows.UI.Xaml.Controls.ISymbolIconFactory].CreateInstanceWithSymbol(symbol, byref(obj))
        return SymbolIcon(obj)

    @classmethod
    @property
    def symbol_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.ISymbolIconStatics].get_SymbolProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def symbol(self) -> enum.Windows.UI.Xaml.Controls.Symbol:
        value = enum.Windows.UI.Xaml.Controls.Symbol()
        self[interface.Windows.UI.Xaml.Controls.ISymbolIcon].get_Symbol(byref(value))
        return value

    @symbol.setter
    def symbol(self, value: enum.Windows.UI.Xaml.Controls.Symbol):
        self[interface.Windows.UI.Xaml.Controls.ISymbolIcon].put_Symbol(value)


class _CommandBarElement(_Inspectable):
    _interfaces = (interface.Windows.UI.Xaml.Controls.ICommandBarElement,
                   interface.Windows.UI.Xaml.Controls.ICommandBarElement2)

    @property
    def is_compact(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.ICommandBarElement].get_IsCompact(byref(value))
        return value.value

    @is_compact.setter
    def is_compact(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.ICommandBarElement].put_IsCompact(value)

    @property
    def is_in_overflow(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.ICommandBarElement].get_IsInOverflow(byref(value))
        return value.value

    @property
    def dynamic_overflow_order(self) -> int:
        value = type.INT32()
        self[interface.Windows.UI.Xaml.Controls.ICommandBarElement].get_DynamicOverflowOrder(byref(value))
        return value.value

    @dynamic_overflow_order.setter
    def dynamic_overflow_order(self, value: int):
        self[interface.Windows.UI.Xaml.Controls.ICommandBarElement].put_DynamicOverflowOrder(value)


class AppBarButton(_CommandBarElement, _ButtonWithFlyout, ButtonBase):
    _statics = (interface.Windows.UI.Xaml.Controls.IAppBarButtonFactory,
                interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics,
                interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics3,
                interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics4)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IAppBarButton,
                   interface.Windows.UI.Xaml.Controls.IAppBarButton3,
                   interface.Windows.UI.Xaml.Controls.IAppBarButton4,
                   interface.Windows.UI.Xaml.Controls.IAppBarButton5)

    @classmethod
    @property
    def label_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics].get_LabelProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def icon_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics].get_IconProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_compact_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics].get_IsCompactProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def label_position_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics3].get_LabelPositionProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_in_overflow_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics3].get_IsInOverflowProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def dynamic_overflow_order_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics3].get_DynamicOverflowOrderProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_text_override_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IAppBarButtonStatics4].get_KeyboardAcceleratorTextOverrideProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def label(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton].get_Label(byref(value))
        return value.value

    @label.setter
    def label(self, value: str):
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton].put_Label(HSTRING.from_string(value))

    @property
    def icon(self) -> IconElement:
        obj = interface.Windows.UI.Xaml.Controls.IIconElement()
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton].get_Icon(byref(obj))
        return IconElement(obj)

    @icon.setter
    def icon(self, value: IconElement):
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton].put_Icon(value[interface.Windows.UI.Xaml.Controls.IIconElement])

    @property
    def label_position(self) -> enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition:
        value = enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition()
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton3].get_LabelPosition(byref(value))
        return value

    @label_position.setter
    def label_position(self, value: enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition):
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton3].put_LabelPosition(value)

    @property
    def keyboard_accelerator_text_override(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton4].get_KeyboardAcceleratorTextOverride(byref(value))
        return value.value

    @keyboard_accelerator_text_override.setter
    def keyboard_accelerator_text_override(self, value: str):
        self[interface.Windows.UI.Xaml.Controls.IAppBarButton4].put_KeyboardAcceleratorTextOverride(HSTRING.from_string(value))


class ToolTip(ContentControl):
    _statics = (interface.Windows.UI.Xaml.Controls.IToolTipFactory,
                interface.Windows.UI.Xaml.Controls.IToolTipStatics,
                interface.Windows.UI.Xaml.Controls.IToolTipStatics2)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IToolTip,
                   interface.Windows.UI.Xaml.Controls.IToolTip2)

    @classmethod
    @property
    def horizontal_offset_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics].get_HorizontalOffsetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def is_open_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics].get_IsOpenProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def placement_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics].get_PlacementProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def placement_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics].get_PlacementTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def vertical_offset_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics].get_VerticalOffsetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    @property
    def placement_rect_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipStatics2].get_PlacementRectProperty(byref(obj))
        return DependencyProperty(obj)

    @property
    def horizontal_offset(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.Controls.IToolTip].get_HorizontalOffset(byref(value))
        return value.value

    @horizontal_offset.setter
    def horizontal_offset(self, value: float):
        self[interface.Windows.UI.Xaml.Controls.IToolTip].put_HorizontalOffset(value)

    @property
    def is_open(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Xaml.Controls.IToolTip].get_IsOpen(byref(value))
        return value.value

    @is_open.setter
    def is_open(self, value: bool):
        self[interface.Windows.UI.Xaml.Controls.IToolTip].put_IsOpen(value)

    @property
    def placement(self) -> enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode()
        self[interface.Windows.UI.Xaml.Controls.IToolTip].get_Placement(byref(value))
        return value

    @placement.setter
    def placement(self, value: enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode):
        self[interface.Windows.UI.Xaml.Controls.IToolTip].put_Placement(value)

    @property
    def placement_target(self) -> UIElement:
        obj = interface.Windows.UI.Xaml.IUIElement()
        self[interface.Windows.UI.Xaml.Controls.IToolTip].get_PlacementTarget(byref(obj))
        return UIElement(obj)

    @placement_target.setter
    def placement_target(self, value: UIElement):
        self[interface.Windows.UI.Xaml.Controls.IToolTip].put_PlacementTarget(value[interface.Windows.UI.Xaml.IUIElement])

    @property
    def vertical_offset(self) -> float:
        value = type.DOUBLE()
        self[interface.Windows.UI.Xaml.Controls.IToolTip].get_VerticalOffset(byref(value))
        return value.value

    @vertical_offset.setter
    def vertical_offset(self, value: float):
        self[interface.Windows.UI.Xaml.Controls.IToolTip].put_VerticalOffset(value)


class ToolTipService(_Inspectable):
    _statics = (interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics,)
    _interfaces = (interface.Windows.UI.Xaml.Controls.IToolTipService,)

    @classmethod
    @property
    def placement_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].get_PlacementProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    def get_placement(cls, element: DependencyObject) -> enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode:
        value = enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].GetPlacement(element[interface.Windows.UI.Xaml.IDependencyObject], byref(value))
        return value

    @classmethod
    def set_placement(cls, element: DependencyObject, value: enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].SetPlacement(element[interface.Windows.UI.Xaml.IDependencyObject], value))

    @classmethod
    @property
    def placement_target_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].get_PlacementTargetProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    def get_placement_target(cls, element: DependencyObject) -> UIElement:
        obj = interface.Windows.UI.Xaml.IUIElement()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].GetPlacementTarget(element[interface.Windows.UI.Xaml.IDependencyObject], byref(obj))
        return UIElement(obj)

    @classmethod
    def set_placement_target(cls, element: DependencyObject, value: UIElement) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].SetPlacementTarget(element[interface.Windows.UI.Xaml.IDependencyObject], value[interface.Windows.UI.Xaml.IUIElement]))

    @classmethod
    @property
    def tool_tip_property(cls) -> DependencyProperty:
        obj = interface.Windows.UI.Xaml.IDependencyProperty()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].get_ToolTipProperty(byref(obj))
        return DependencyProperty(obj)

    @classmethod
    def get_tool_tip(cls, element: DependencyObject) -> _Inspectable:
        obj = interface.IInspectable()
        cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].GetToolTip(element[interface.Windows.UI.Xaml.IDependencyObject], byref(obj))
        return _Inspectable(obj)

    @classmethod
    def set_tool_tip(cls, element: DependencyObject, value: _Inspectable) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Xaml.Controls.IToolTipServiceStatics].SetToolTip(element[interface.Windows.UI.Xaml.IDependencyObject], value[interface.IInspectable]))


class _XmlDocumentIO(_Inspectable):
    _interfaces = (interface.Windows.Data.Xml.Dom.IXmlDocumentIO,
                   interface.Windows.Data.Xml.Dom.IXmlDocumentIO2)

    def load_xml(self, xml: str) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Data.Xml.Dom.IXmlDocumentIO].LoadXml(HSTRING.from_string(xml)))


class XmlDocument(_XmlDocumentIO):
    _statics = (interface.Windows.Data.Xml.Dom.IXmlDocumentStatics,)
    _interfaces = (interface.Windows.Data.Xml.Dom.IXmlDocument,)

    @property
    def document_uri(self) -> str:
        value = HSTRING()
        self[interface.Windows.Data.Xml.Dom.IXmlDocument].get_DocumentUri(byref(value))
        return value.value


class ToastNotificationManager(_Inspectable):
    _statics = (interface.Windows.UI.Notifications.IToastNotificationManagerStatics,
                interface.Windows.UI.Notifications.IToastNotificationManagerStatics2,
                interface.Windows.UI.Notifications.IToastNotificationManagerStatics4,
                interface.Windows.UI.Notifications.IToastNotificationManagerStatics5)

    @classmethod
    def create_toast_notifier(cls) -> ToastNotifier:
        obj = interface.Windows.UI.Notifications.IToastNotifier()
        cls[interface.Windows.UI.Notifications.IToastNotificationManagerStatics].CreateToastNotifier(byref(obj))
        return ToastNotifier(obj)

    @classmethod
    def create_toast_notifier_with_id(cls, application_id: str) -> ToastNotifier:
        obj = interface.Windows.UI.Notifications.IToastNotifier()
        cls[interface.Windows.UI.Notifications.IToastNotificationManagerStatics].CreateToastNotifierWithId(HSTRING.from_string(application_id), byref(obj))
        return ToastNotifier(obj)

    # noinspection PyShadowingBuiltins,PyShadowingNames
    @classmethod
    def get_template_content(cls, type: enum.Windows.UI.Notifications.ToastTemplateType) -> XmlDocument:
        obj = interface.Windows.Data.Xml.Dom.IXmlDocument()
        cls[interface.Windows.UI.Notifications.IToastNotificationManagerStatics].GetTemplateContent(type, byref(obj))
        return XmlDocument(obj)

    @classmethod
    def configure_notification_mirroring(cls, value: enum.Windows.UI.Notifications.NotificationMirroring) -> bool:
        return macro.SUCCEEDED(cls[interface.Windows.UI.Notifications.IToastNotificationManagerStatics4].ConfigureNotificationMirroring(value))


class ToastNotifier(_Inspectable):
    _interfaces = (interface.Windows.UI.Notifications.IToastNotifier,
                   interface.Windows.UI.Notifications.IToastNotifier2,
                   interface.Windows.UI.Notifications.IToastNotifier3)

    def show(self, notification: ToastNotification) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Notifications.IToastNotifier].Show(notification[interface.Windows.UI.Notifications.IToastNotification]))

    def hide(self, notification: ToastNotification) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.UI.Notifications.IToastNotifier].Hide(notification[interface.Windows.UI.Notifications.IToastNotification]))

    @property
    def setting(self) -> enum.Windows.UI.Notifications.NotificationSetting:
        value = enum.Windows.UI.Notifications.NotificationSetting()
        self[interface.Windows.UI.Notifications.IToastNotifier].get_Setting(byref(value))
        return value


class ToastNotification(_Inspectable):
    _statics = (interface.Windows.UI.Notifications.IToastNotificationFactory,)
    _interfaces = (interface.Windows.UI.Notifications.IToastNotification,
                   interface.Windows.UI.Notifications.IToastNotification2,
                   interface.Windows.UI.Notifications.IToastNotification3,
                   interface.Windows.UI.Notifications.IToastNotification4,
                   interface.Windows.UI.Notifications.IToastNotification6)

    @classmethod
    def create_toast_notification(cls, content: XmlDocument) -> ToastNotification:
        obj = interface.Windows.UI.Notifications.IToastNotification()
        cls[interface.Windows.UI.Notifications.IToastNotificationFactory].CreateToastNotification(content[interface.Windows.Data.Xml.Dom.IXmlDocument], byref(obj))
        return ToastNotification(obj)

    @property
    def content(self) -> XmlDocument:
        obj = interface.Windows.Data.Xml.Dom.IXmlDocument()
        self[interface.Windows.UI.Notifications.IToastNotification].get_Content(byref(obj))
        return XmlDocument(obj)

    @property
    def dismissed(self) -> _TypedEventToastNotificationToastDismissedEventArgs:
        return _TypedEventToastNotificationToastDismissedEventArgs(self[interface.Windows.UI.Notifications.IToastNotification], 'Dismissed')

    @dismissed.setter
    def dismissed(self, value: _TypedEventToastNotificationToastDismissedEventArgs):
        pass

    @property
    def activated(self) -> _TypedEventToastNotificationInspectable:
        return _TypedEventToastNotificationInspectable(self[interface.Windows.UI.Notifications.IToastNotification], 'Activated')

    @activated.setter
    def activated(self, value: _TypedEventToastNotificationInspectable):
        pass

    @property
    def failed(self) -> _TypedEventToastNotificationToastFailedEventArgs:
        return _TypedEventToastNotificationToastFailedEventArgs(self[interface.Windows.UI.Notifications.IToastNotification], 'Failed')

    @failed.setter
    def failed(self, value: _TypedEventToastNotificationToastFailedEventArgs):
        pass

    @property
    def tag(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Notifications.IToastNotification2].get_Tag(byref(value))
        return value.value

    @tag.setter
    def tag(self, value: str):
        self[interface.Windows.UI.Notifications.IToastNotification2].put_Tag(HSTRING(value))

    @property
    def group(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Notifications.IToastNotification2].get_Group(byref(value))
        return value.value

    @group.setter
    def group(self, value: str):
        self[interface.Windows.UI.Notifications.IToastNotification2].put_Group(HSTRING(value))

    @property
    def suppress_popup(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Notifications.IToastNotification2].get_SuppressPopup(byref(value))
        return value.value

    @suppress_popup.setter
    def suppress_popup(self, value: bool):
        self[interface.Windows.UI.Notifications.IToastNotification2].put_SuppressPopup(value)

    @property
    def notification_mirroring(self) -> enum.Windows.UI.Notifications.NotificationMirroring:
        value = enum.Windows.UI.Notifications.NotificationMirroring()
        self[interface.Windows.UI.Notifications.IToastNotification3].get_NotificationMirroring(byref(value))
        return value

    @notification_mirroring.setter
    def notification_mirroring(self, value: enum.Windows.UI.Notifications.NotificationMirroring):
        self[interface.Windows.UI.Notifications.IToastNotification3].put_NotificationMirroring(value)

    @property
    def remote_id(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Notifications.IToastNotification3].get_RemoteId(byref(value))
        return value.value

    @remote_id.setter
    def remote_id(self, value: str):
        self[interface.Windows.UI.Notifications.IToastNotification3].put_RemoteId(HSTRING(value))

    @property
    def priority(self) -> enum.Windows.UI.Notifications.ToastNotificationPriority:
        value = enum.Windows.UI.Notifications.ToastNotificationPriority()
        self[interface.Windows.UI.Notifications.IToastNotification4].get_Priority(byref(value))
        return value

    @priority.setter
    def priority(self, value: enum.Windows.UI.Notifications.ToastNotificationPriority):
        self[interface.Windows.UI.Notifications.IToastNotification4].put_Priority(value)

    @property
    def expires_on_reboot(self) -> bool:
        value = boolean()
        self[interface.Windows.UI.Notifications.IToastNotification6].get_ExpiresOnReboot(byref(value))
        return value.value

    @expires_on_reboot.setter
    def expires_on_reboot(self, value: bool):
        self[interface.Windows.UI.Notifications.IToastNotification6].put_ExpiresOnReboot(value)


class ToastDismissedEventArgs(_Inspectable):
    _interfaces = (interface.Windows.UI.Notifications.IToastDismissedEventArgs,)

    @property
    def reason(self) -> enum.Windows.UI.Notifications.ToastDismissalReason:
        value = enum.Windows.UI.Notifications.ToastDismissalReason()
        self[interface.Windows.UI.Notifications.IToastDismissedEventArgs].get_Reason(byref(value))
        return value


class ToastActivatedEventArgs(_Inspectable):
    _interfaces = (interface.Windows.UI.Notifications.IToastActivatedEventArgs,
                   interface.Windows.UI.Notifications.IToastActivatedEventArgs2)

    @property
    def argument(self) -> str:
        value = HSTRING()
        self[interface.Windows.UI.Notifications.IToastActivatedEventArgs].get_Argument(byref(value))
        return value.value


class ToastFailedEventArgs(_Inspectable):
    _interfaces = (interface.Windows.UI.Notifications.IToastFailedEventArgs,)

    @property
    def error_code(self) -> int:
        value = type.HRESULT()
        self[interface.Windows.UI.Notifications.IToastFailedEventArgs].get_ErrorCode(byref(value))
        return value.value


class _ITypedEventHandler(_Unknown):
    _tsender_typed_event_handler: tuple
    _targs_typed_event_handler: tuple
    _handlers = {}

    @classmethod
    def create_instance(cls, function: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        handler = cls._tsender_typed_event_handler[0], cls._targs_typed_event_handler[0]
        if handler not in cls._handlers:
            class TypedEventHandler(interface.Windows.Foundation.ITypedEventHandler_impl[handler]):
                function: Callable
                args: Iterable
                kwargs: Mapping[str, Any]

                # noinspection PyPep8Naming,PyShadowingNames
                def Invoke(self, sender, args) -> type.HRESULT:
                    return self.function(cls._tsender_typed_event_handler[1](sender), cls._targs_typed_event_handler[1](args), *self.args, **self.kwargs)

            cls._handlers[handler] = TypedEventHandler
        obj = cls._handlers[handler]()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return cls(obj)

    def __call__(self, sender, args) -> type.HRESULT:
        handler = self._tsender_typed_event_handler[0], self._targs_typed_event_handler[0]
        return self[interface.Windows.Foundation.ITypedEventHandler[handler]].Invoke(sender[handler[0]], args[handler[1]])


class TypedEventHandlerToastNotificationToastDismissedEventArgs(_ITypedEventHandler):
    _tsender_typed_event_handler = interface.Windows.UI.Notifications.IToastNotification, ToastNotification
    _targs_typed_event_handler = interface.Windows.UI.Notifications.IToastDismissedEventArgs, ToastDismissedEventArgs
    _interfaces = (interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.Windows.UI.Notifications.IToastDismissedEventArgs],)

    create_instance: Callable[[Callable[[ToastNotification, ToastDismissedEventArgs, ...], type.HRESULT], Optional[Iterable], Optional[Mapping[str, Any]]], TypedEventHandlerToastNotificationToastDismissedEventArgs]
    __call__: Callable[[ToastNotification, ToastDismissedEventArgs], type.HRESULT]


class TypedEventHandlerToastNotificationInspectable(_ITypedEventHandler):
    _tsender_typed_event_handler = interface.Windows.UI.Notifications.IToastNotification, ToastNotification
    _targs_typed_event_handler = interface.IInspectable, _Inspectable
    _interfaces = (interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.IInspectable],)

    create_instance: Callable[[Callable[[ToastNotification, _Inspectable, ...], type.HRESULT], Optional[Iterable], Optional[Mapping[str, Any]]], TypedEventHandlerToastNotificationInspectable]
    __call__: Callable[[ToastNotification, _Inspectable], type.HRESULT]


class TypedEventHandlerToastNotificationToastFailedEventArgs(_ITypedEventHandler):
    _tsender_typed_event_handler = interface.Windows.UI.Notifications.IToastNotification, ToastNotification
    _targs_typed_event_handler = interface.Windows.UI.Notifications.IToastFailedEventArgs, ToastFailedEventArgs
    _interfaces = (interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.Windows.UI.Notifications.IToastFailedEventArgs],)

    create_instance: Callable[[Callable[[ToastNotification, ToastFailedEventArgs, ...], type.HRESULT], Optional[Iterable], Optional[Mapping[str, Any]]], TypedEventHandlerToastNotificationToastFailedEventArgs]
    __call__: Callable[[ToastNotification, ToastFailedEventArgs], type.HRESULT]


class _InputStream(_Closable):
    _interfaces = (interface.Windows.Storage.Streams.IInputStream,)


class FileInputStream(_InputStream):
    pass


class _OutputStream(_Closable):
    _interfaces = (interface.Windows.Storage.Streams.IOutputStream,)


class FileOutputStream(_OutputStream):
    pass


class RandomAccessStream(_InputStream, _OutputStream):
    _statics = (interface.Windows.Storage.Streams.IRandomAccessStreamStatics,)
    _interfaces = (interface.Windows.Storage.Streams.IRandomAccessStream,)

    @classmethod
    def copy_async(cls, source: _InputStream, destination: _OutputStream) -> AsyncOperationWithProgressUINT64UINT64:
        obj = interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64]()
        cls[interface.Windows.Storage.Streams.IRandomAccessStreamStatics].CopyAsync(source[interface.Windows.Storage.Streams.IInputStream], destination[interface.Windows.Storage.Streams.IOutputStream], byref(obj))
        return AsyncOperationWithProgressUINT64UINT64(obj)

    @classmethod
    def copy_size_async(cls, source: FileInputStream, destination: FileOutputStream, bytes_to_copy: int) -> AsyncOperationWithProgressUINT64UINT64:
        obj = interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64]()
        cls[interface.Windows.Storage.Streams.IRandomAccessStreamStatics].CopySizeAsync(source[interface.Windows.Storage.Streams.IInputStream], destination[interface.Windows.Storage.Streams.IOutputStream], bytes_to_copy, byref(obj))
        return AsyncOperationWithProgressUINT64UINT64(obj)

    @classmethod
    def copy_and_close_async(cls, source: FileInputStream, destination: FileOutputStream) -> AsyncOperationWithProgressUINT64UINT64:
        obj = interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64]()
        cls[interface.Windows.Storage.Streams.IRandomAccessStreamStatics].CopyAndCloseAsync(source[interface.Windows.Storage.Streams.IInputStream], destination[interface.Windows.Storage.Streams.IOutputStream], byref(obj))
        return AsyncOperationWithProgressUINT64UINT64(obj)

    @property
    def size(self) -> int:
        value = type.UINT64()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].get_Size(byref(value))
        return value.value

    @size.setter
    def size(self, value: int):
        self[interface.Windows.Storage.Streams.IRandomAccessStream].put_Size(type.UINT64(value))

    def get_input_stream_at(self, position: int) -> FileInputStream:
        value = interface.Windows.Storage.Streams.IInputStream()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].GetInputStreamAt(position, byref(value))
        return FileInputStream(value)

    def get_output_stream_at(self, position: int) -> FileOutputStream:
        value = interface.Windows.Storage.Streams.IOutputStream()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].GetOutputStreamAt(position, byref(value))
        return FileOutputStream(value)

    @property
    def position(self) -> int:
        value = type.UINT64()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].get_Position(byref(value))
        return value.value

    def seek(self, position: int) -> bool:
        return macro.SUCCEEDED(self[interface.Windows.Storage.Streams.IRandomAccessStream].Seek(type.UINT64(position)))

    @property
    def can_read(self) -> bool:
        value = boolean()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].get_CanRead(byref(value))
        return value.value

    @property
    def can_write(self) -> bool:
        value = boolean()
        self[interface.Windows.Storage.Streams.IRandomAccessStream].get_CanWrite(byref(value))
        return value.value


class FileRandomAccessStream(RandomAccessStream):
    _statics = (interface.Windows.Storage.Streams.IFileRandomAccessStreamStatics,)

    @classmethod
    def open_async(cls, file_path: str, access_mode: enum.Windows.Storage.FileAccessMode) -> AsyncOperationRandomAccessStream:
        value = interface.Windows.Foundation.IAsyncOperation[interface.Windows.Storage.Streams.IRandomAccessStream]()
        cls[interface.Windows.Storage.Streams.IFileRandomAccessStreamStatics].OpenAsync(HSTRING.from_string(file_path), access_mode, byref(value))
        return AsyncOperationRandomAccessStream(value)

    @classmethod
    def open_with_options_async(cls, file_path: str, access_mode: enum.Windows.Storage.FileAccessMode, sharing_options: enum.Windows.Storage.StorageOpenOptions,
                                open_disposition: enum.Windows.Storage.Streams.FileOpenDisposition) -> AsyncOperationRandomAccessStream:
        value = interface.Windows.Foundation.IAsyncOperation[interface.Windows.Storage.Streams.IRandomAccessStream]()
        cls[interface.Windows.Storage.Streams.IFileRandomAccessStreamStatics].OpenWithOptionsAsync(HSTRING.from_string(file_path), access_mode, sharing_options, open_disposition, byref(value))
        return AsyncOperationRandomAccessStream(value)


class _IAsyncOperationProgressHandler(_Unknown):
    _tasync_info_async_operation_progress_handler: tuple
    _handlers = {}

    @classmethod
    def create_instance(cls, function: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        # noinspection PyProtectedMember
        types = tuple(cls._tasync_info_async_operation_progress_handler[0]._args.values())
        if types not in cls._handlers:
            class AsyncOperationProgressHandler(interface.Windows.Foundation.IAsyncOperationProgressHandler_impl[types]):
                function: Callable
                args: Iterable
                kwargs: Mapping[str, Any]

                # noinspection PyPep8Naming,PyShadowingNames
                def Invoke(self, async_info, progress_info) -> type.HRESULT:
                    # noinspection PyProtectedMember
                    return self.function(cls._tasync_info_async_operation_progress_handler[1](
                        async_info), cls._tasync_info_async_operation_progress_handler[1]._tprogress_async_operation_with_progress[1](progress_info), *self.args, **self.kwargs)

            cls._handlers[types] = AsyncOperationProgressHandler
        obj = cls._handlers[types]()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return cls(obj)

    def __call__(self, async_info, progress_info) -> type.HRESULT:
        # noinspection PyProtectedMember
        return self[interface.Windows.Foundation.IAsyncOperationProgressHandler[tuple(
            self._tasync_info_async_operation_progress_handler[0]._args.values())]].Invoke(async_info[self._tasync_info_async_operation_progress_handler[0]], progress_info)


class _IAsyncOperationWithProgressCompletedHandler(_Unknown):
    _tasync_info_async_operation_with_progress_completed_handler: tuple
    _handlers = {}

    @classmethod
    def create_instance(cls, function: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        # noinspection PyProtectedMember
        types = tuple(cls._tasync_info_async_operation_with_progress_completed_handler[0]._args.values())
        if types not in cls._handlers:
            class AsyncOperationWithProgressCompletedHandler(interface.Windows.Foundation.IAsyncOperationWithProgressCompletedHandler_impl[types]):
                function: Callable
                args: Iterable
                kwargs: Mapping[str, Any]

                # noinspection PyPep8Naming,PyShadowingNames
                def Invoke(self, async_info, status: enum.Windows.Foundation.AsyncStatus) -> type.HRESULT:
                    return self.function(cls._tasync_info_async_operation_with_progress_completed_handler[1](async_info), status, *self.args, **self.kwargs)

            cls._handlers[types] = AsyncOperationWithProgressCompletedHandler
        obj = cls._handlers[types]()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return cls(obj)

    def __call__(self, async_info, status: enum.Windows.Foundation.AsyncStatus) -> type.HRESULT:
        # noinspection PyProtectedMember
        return self[interface.Windows.Foundation.IAsyncOperationWithProgressCompletedHandler[tuple(
            self._tasync_info_async_operation_with_progress_completed_handler[0]._args.values())]].Invoke(async_info[self._tasync_info_async_operation_with_progress_completed_handler[0]], status)


class _IAsyncOperationWithProgress(_Inspectable):
    _tprogress_handler_async_operation_with_progress: tuple
    _tcompleted_handler_async_operation_with_progress: tuple
    _tresult_async_operation_with_progress: tuple
    _tprogress_async_operation_with_progress: tuple

    @property
    def progress(self) -> _IAsyncOperationProgressHandler:
        handler = self._tprogress_handler_async_operation_with_progress[0]()
        self[interface.Windows.Foundation.IAsyncOperationWithProgress[self._tresult_async_operation_with_progress[0], self._tprogress_async_operation_with_progress[0]]].get_Progress(byref(handler))
        return self._tprogress_handler_async_operation_with_progress[1](handler)

    @progress.setter
    def progress(self, handler: _IAsyncOperationProgressHandler):
        self[interface.Windows.Foundation.IAsyncOperationWithProgress[self._tresult_async_operation_with_progress[0], self._tprogress_async_operation_with_progress[0]]].put_Progress(
            handler[self._tprogress_handler_async_operation_with_progress[0]])

    @property
    def completed(self) -> _IAsyncOperationWithProgressCompletedHandler:
        handler = self._tcompleted_handler_async_operation_with_progress[0]()
        self[interface.Windows.Foundation.IAsyncOperationWithProgress[self._tresult_async_operation_with_progress[0], self._tprogress_async_operation_with_progress[0]]].get_Completed(byref(handler))
        return self._tcompleted_handler_async_operation_with_progress[1](handler)

    @completed.setter
    def completed(self, handler: _IAsyncOperationWithProgressCompletedHandler):
        self[interface.Windows.Foundation.IAsyncOperationWithProgress[self._tresult_async_operation_with_progress[0], self._tprogress_async_operation_with_progress[0]]].put_Completed(
            handler[self._tcompleted_handler_async_operation_with_progress[0]])

    def get_results(self):
        obj = self._tresult_async_operation_with_progress[0]()
        self[interface.Windows.Foundation.IAsyncOperationWithProgress[self._tresult_async_operation_with_progress[0]]].GetResults(byref(obj))
        return obj if self._tresult_async_operation_with_progress[1] is None else self._tresult_async_operation_with_progress[1](obj)


class AsyncOperationWithProgressUINT64UINT64(_IAsyncOperationWithProgress):
    _tresult_async_operation_with_progress = type.UINT64, int
    _tprogress_async_operation_with_progress = type.UINT64, int
    _interfaces = (interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64],)

    progress: AsyncOperationProgressHandlerUINT64UINT64
    completed: AsyncOperationWithProgressCompletedHandlerUINT64UINT64
    get_results: Callable[[], int]


class AsyncOperationProgressHandlerUINT64UINT64(_IAsyncOperationProgressHandler):
    _tasync_info_async_operation_progress_handler = interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64], AsyncOperationWithProgressUINT64UINT64
    _interfaces = (interface.Windows.Foundation.IAsyncOperationProgressHandler[type.UINT64, type.UINT64],)

    create_instance: Callable[[Callable[[AsyncOperationWithProgressUINT64UINT64, int], type.HRESULT], Optional[Iterable], Optional[Mapping[str, Any]]], AsyncOperationProgressHandlerUINT64UINT64]
    __call__: Callable[[AsyncOperationWithProgressUINT64UINT64, int], type.HRESULT]


class AsyncOperationWithProgressCompletedHandlerUINT64UINT64(_IAsyncOperationWithProgressCompletedHandler):
    _tasync_info_async_operation_with_progress_completed_handler = interface.Windows.Foundation.IAsyncOperationWithProgress[type.UINT64, type.UINT64], AsyncOperationWithProgressUINT64UINT64
    _interfaces = (interface.Windows.Foundation.IAsyncOperationWithProgressCompletedHandler[type.UINT64, type.UINT64],)

    create_instance: Callable[[Callable[[AsyncOperationWithProgressUINT64UINT64, enum.Windows.Foundation.AsyncStatus, ...], type.HRESULT],
                               Optional[Iterable], Optional[Mapping[str, Any]]], AsyncOperationWithProgressCompletedHandlerUINT64UINT64]
    __call__: Callable[[AsyncOperationWithProgressUINT64UINT64, enum.Windows.Foundation.AsyncStatus], type.HRESULT]


AsyncOperationWithProgressUINT64UINT64._tprogress_handler_async_operation_with_progress = interface.Windows.Foundation.IAsyncOperationProgressHandler[
                                                                                              type.UINT64, type.UINT64], AsyncOperationProgressHandlerUINT64UINT64
AsyncOperationWithProgressUINT64UINT64._tcompleted_handler_async_operation_with_progress = interface.Windows.Foundation.IAsyncOperationWithProgressCompletedHandler[
                                                                                               type.UINT64, type.UINT64], AsyncOperationWithProgressCompletedHandlerUINT64UINT64


class _IAsyncOperationCompletedHandler(_Unknown):
    _tasync_info_async_operation_completed_handler: tuple
    _handlers = {}

    @classmethod
    def create_instance(cls, function: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        # noinspection PyProtectedMember
        types = tuple(cls._tasync_info_async_operation_completed_handler[0]._args.values())
        if types not in cls._handlers:
            class AsyncOperationCompletedHandler(interface.Windows.Foundation.IAsyncOperationCompletedHandler_impl[types]):
                function: Callable
                args: Iterable
                kwargs: Mapping[str, Any]

                # noinspection PyPep8Naming,PyShadowingNames
                def Invoke(self, async_info, status: enum.Windows.Foundation.AsyncStatus) -> type.HRESULT:
                    return self.function(cls._tasync_info_async_operation_completed_handler[1](async_info), status, *self.args, **self.kwargs)

            cls._handlers[types] = AsyncOperationCompletedHandler
        obj = cls._handlers[types]()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return cls(obj)

    def __call__(self, async_info, status: enum.Windows.Foundation.AsyncStatus) -> type.HRESULT:
        # noinspection PyProtectedMember
        return self[interface.Windows.Foundation.IAsyncOperationCompletedHandler[tuple(
            self._tasync_info_async_operation_completed_handler[0]._args.values())]].Invoke(async_info[self._tasync_info_async_operation_completed_handler[0]], status)


class _IAsyncOperation(_Inspectable):
    _tcompleted_async_operation_completed: tuple
    _tresult_async_operation: tuple

    @property
    def completed(self) -> _IAsyncOperationCompletedHandler:
        handler = self._tcompleted_async_operation_completed[0]()
        self[interface.Windows.Foundation.IAsyncOperation[self._tresult_async_operation[0]]].get_Completed(byref(handler))
        return self._tcompleted_async_operation_completed[1](handler)

    @completed.setter
    def completed(self, handler: _IAsyncOperationCompletedHandler):
        self[interface.Windows.Foundation.IAsyncOperation[self._tresult_async_operation[0]]].put_Completed(handler[self._tcompleted_async_operation_completed[0]])

    def get_results(self):
        obj = self._tresult_async_operation[0]()
        self[interface.Windows.Foundation.IAsyncOperation[self._tresult_async_operation[0]]].GetResults(byref(obj))
        return obj if self._tresult_async_operation[1] is None else self._tresult_async_operation[1](obj)


class AsyncOperationRandomAccessStream(_IAsyncOperation):
    _tresult_async_operation = interface.Windows.Storage.Streams.IRandomAccessStream, RandomAccessStream
    _interfaces = (interface.Windows.Foundation.IAsyncOperation[interface.Windows.Storage.Streams.IRandomAccessStream],)

    completed: AsyncOperationCompletedHandlerRandomAccessStream
    get_results: Callable[[], RandomAccessStream]


class AsyncOperationCompletedHandlerRandomAccessStream(_IAsyncOperationCompletedHandler):
    _tasync_info_async_operation_completed_handler = interface.Windows.Foundation.IAsyncOperation[interface.Windows.Storage.Streams.IRandomAccessStream], AsyncOperationRandomAccessStream
    _interfaces = (interface.Windows.Foundation.IAsyncOperationCompletedHandler[interface.Windows.Storage.Streams.IRandomAccessStream],)

    create_instance: Callable[[Callable[[AsyncOperationRandomAccessStream, enum.Windows.Foundation.AsyncStatus, ...], type.HRESULT], Optional[Iterable], Optional[Mapping[str, Any]]], AsyncOperationCompletedHandlerRandomAccessStream]
    __call__: Callable[[AsyncOperationRandomAccessStream, enum.Windows.Foundation.AsyncStatus], type.HRESULT]


AsyncOperationRandomAccessStream._tcompleted_async_operation_completed = interface.Windows.Foundation.IAsyncOperationCompletedHandler[interface.Windows.Storage.Streams.IRandomAccessStream], AsyncOperationCompletedHandlerRandomAccessStream


class _Event:
    _interface: interface.IInspectable
    _tokens = {}

    def __init__(self, obj: interface.IInspectable, attr: str):
        self._add = getattr(obj, f'add_{attr}')
        self._remove = getattr(obj, f'remove_{attr}')

    def __iadd__(self, other) -> _Event:
        value = struct.EventRegistrationToken()
        if macro.SUCCEEDED(self._add(other[self._interface], byref(value))):
            self._tokens[other] = value
        return self

    def __isub__(self, other) -> _Event:
        if macro.SUCCEEDED(self._remove(self._tokens[other])):
            del self._tokens[other]
        return self


class _RoutedEvent(_Event):
    _interface = interface.Windows.UI.Xaml.IRoutedEventHandler

    __iadd__: Callable[[RoutedEventHandler], _RoutedEvent]
    __isub__: Callable[[RoutedEventHandler], _RoutedEvent]


class _TypedEventToastNotificationToastDismissedEventArgs(_Event):
    _interface = interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.Windows.UI.Notifications.IToastDismissedEventArgs]

    __iadd__: Callable[[TypedEventHandlerToastNotificationToastDismissedEventArgs], _TypedEventToastNotificationToastDismissedEventArgs]
    __isub__: Callable[[TypedEventHandlerToastNotificationToastDismissedEventArgs], _TypedEventToastNotificationToastDismissedEventArgs]


class _TypedEventToastNotificationInspectable(_Event):
    _interface = interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.IInspectable]

    __iadd__: Callable[[TypedEventHandlerToastNotificationInspectable], _TypedEventToastNotificationInspectable]
    __isub__: Callable[[TypedEventHandlerToastNotificationInspectable], _TypedEventToastNotificationInspectable]


class _TypedEventToastNotificationToastFailedEventArgs(_Event):
    _interface = interface.Windows.Foundation.ITypedEventHandler[interface.Windows.UI.Notifications.IToastNotification, interface.Windows.UI.Notifications.IToastFailedEventArgs]

    __iadd__: Callable[[TypedEventHandlerToastNotificationToastFailedEventArgs], _TypedEventToastNotificationToastFailedEventArgs]
    __isub__: Callable[[TypedEventHandlerToastNotificationToastFailedEventArgs], _TypedEventToastNotificationToastFailedEventArgs]
