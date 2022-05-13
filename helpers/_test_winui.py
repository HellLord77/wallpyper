from __future__ import annotations as _

import atexit
import builtins as _builtins
import contextlib as _contextlib
from typing import ContextManager as _ContextManager, Optional as _Optional, TypeVar as _TypeVar, Callable as _Callable, Iterable as _Iterable, Mapping as _Mapping, Any as _Any

from libs import ctyped

winrt = ctyped.interface.Windows

_HWND = None

_T = _TypeVar('_T', bound=ctyped.interface.IUnknown)


class _Interface(type):
    _interfaces: dict[type[_T], _Optional[_T]]
    _statics: dict[type[_T], _Optional[_T]]
    ctyped.lib.Combase.RoInitialize(ctyped.enum.RO_INIT_TYPE.SINGLETHREADED)
    atexit.register(ctyped.lib.Combase.RoUninitialize)

    def __del__(self):  # TODO
        if isinstance(self._statics, dict):
            for static, obj in self._statics.items():
                if obj:
                    obj.Release()
                    self._statics[static] = None

    def __getitem__(self, item: type[_T]) -> _Optional[_T]:
        if self._statics[item] is None:
            with ctyped.get_winrt(item) as obj:
                if obj:
                    obj.AddRef()
                    self._statics[item] = obj
        return self._statics[item]


class _Unknown(metaclass=_Interface):
    _self: _Optional[_T] = None
    _statics = {}
    _interfaces = {ctyped.interface.IUnknown: None}

    def __init_subclass__(cls):
        cls._statics = {static: None for static in cls._statics}
        # noinspection PyProtectedMember,PyUnresolvedReferences
        cls._statics.update(cls.__base__._statics)
        cls._interfaces = {interface: None for interface in cls._interfaces}
        for base in cls.__mro__[:-1]:
            # noinspection PyProtectedMember,PyUnresolvedReferences
            cls._interfaces.update({interface: None for interface in base._interfaces})

    def __init__(self, obj: _Optional = None):  # TODO cache using hash
        if isinstance(obj, Inspectable):
            obj = obj._self
        with ctyped.get_winrt(next(iter(self._interfaces)), True) if obj is None else _contextlib.nullcontext(obj) as obj:
            obj.AddRef()
        self._self = obj
        self._interfaces = self._interfaces.copy()

    def __del__(self):
        if self._self:
            self._self.Release()
            self._self = None
            for interface, obj in self._interfaces.items():
                if obj:
                    obj.Release()
                    self._interfaces[interface] = None

    def __hash__(self):
        return self._self.value

    def __getitem__(self, item: type[_T]) -> _Optional[_T]:
        if self._interfaces[item] is None:
            with _contextlib.nullcontext(self._self) if item is type(self) else ctyped.cast_com(self._self, item) as obj:
                if obj:
                    obj.AddRef()
                    self._interfaces[item] = obj
        return self._interfaces[item]

    def add_ref(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.IUnknown].AddRef())

    def release(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.IUnknown].Release())


class Inspectable(_Unknown):
    _interfaces = (ctyped.interface.IInspectable,)

    def get_runtime_class_name(self) -> ctyped.handle.HSTRING:
        value = ctyped.handle.HSTRING()
        self[ctyped.interface.IInspectable].GetRuntimeClassName(ctyped.byref(value))
        return value

    def get_trust_level(self) -> ctyped.enum.TrustLevel:
        value = ctyped.enum.TrustLevel()
        self[ctyped.interface.IInspectable].GetTrustLevel(ctyped.byref(value))
        return value


class Closable(Inspectable):
    _interfaces = (ctyped.interface.Windows.Foundation.IClosable,)

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.IClosable].Close())


class VisualElement(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Composition.IVisualElement,
                   ctyped.interface.Windows.UI.Composition.IVisualElement2)


class AnimationObject(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Composition.IAnimationObject,)


class ScrollSnapPointsInfo(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo,)

    @property
    def are_horizontal_snap_points_regular(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo].get_AreHorizontalSnapPointsRegular(ctyped.byref(value))
        return value

    @property
    def are_vertical_snap_points_regular(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IScrollSnapPointsInfo].get_AreVerticalSnapPointsRegular(ctyped.byref(value))
        return value


class InsertionPanel(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IInsertionPanel,)


class RoutedEventArgs(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IRoutedEventArgs,)

    @property
    def original_source(self) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.IRoutedEventArgs].get_OriginalSource(ctyped.byref(obj))
            return Inspectable(obj)


class _IRoutedEventHandler(ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler_impl):
    function: _Callable
    args: _Iterable
    kwargs: _Mapping[str, _Any]

    # noinspection PyPep8Naming
    def Invoke(self, sender: ctyped.interface.IInspectable, e: ctyped.interface.Windows.UI.Xaml.IRoutedEventArgs) -> ctyped.type.HRESULT:
        return self.function(Inspectable(sender), RoutedEventArgs(e), *self.args, **self.kwargs)


class RoutedEventHandler(_Unknown):  # TODO not releasing
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler,)

    @classmethod
    def create_instance(cls, function: _Callable[[Inspectable, RoutedEventArgs, ...], ctyped.type.HRESULT], args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None) -> RoutedEventHandler:
        obj = _IRoutedEventHandler()
        obj.function = function
        obj.args = () if args is None else args
        obj.kwargs = {} if kwargs is None else kwargs
        return RoutedEventHandler(obj)

    def __call__(self, sender: Inspectable, e: RoutedEventArgs) -> ctyped.type.HRESULT:
        return self[ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler].Invoke(sender[ctyped.interface.IInspectable], e[ctyped.interface.Windows.UI.Xaml.IRoutedEventArgs])


class CoreDispatcher(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Core.ICoreDispatcher,
                   ctyped.interface.Windows.UI.Core.ICoreDispatcher2)


class DesktopWindowXamlSource(Closable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource,)

    @property
    def content(self) -> UIElement:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IUIElement, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource].get_Content(ctyped.byref(obj))
            return UIElement(obj)

    @content.setter
    def content(self, value: UIElement):
        self[ctyped.interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource].put_Content(value[ctyped.interface.Windows.UI.Xaml.IUIElement])


class WindowsXamlManager(Closable):
    _statics = (ctyped.interface.Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Hosting.IWindowsXamlManager,)

    @classmethod
    def initialize_for_current_thread(cls) -> WindowsXamlManager:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.Hosting.IWindowsXamlManager, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Hosting.IWindowsXamlManagerStatics].InitializeForCurrentThread(ctyped.byref(obj))
            return WindowsXamlManager(obj)


class DependencyObject(Inspectable):
    _statics = (ctyped.interface.Windows.UI.Xaml.IDependencyObjectFactory,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IDependencyObject,
                   ctyped.interface.Windows.UI.Xaml.IDependencyObject2)


class UIElement(AnimationObject, VisualElement, DependencyObject):
    _statics = (ctyped.interface.Windows.UI.Xaml.IUIElementStatics,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics10,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics2,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics3,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics4,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics5,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics6,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics7,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics8,
                ctyped.interface.Windows.UI.Xaml.IUIElementStatics9)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IUIElement,
                   ctyped.interface.Windows.UI.Xaml.IUIElement2,
                   ctyped.interface.Windows.UI.Xaml.IUIElement3,
                   ctyped.interface.Windows.UI.Xaml.IUIElement4,
                   ctyped.interface.Windows.UI.Xaml.IUIElement5,
                   ctyped.interface.Windows.UI.Xaml.IUIElement7,
                   ctyped.interface.Windows.UI.Xaml.IUIElement8,
                   ctyped.interface.Windows.UI.Xaml.IUIElement9,
                   ctyped.interface.Windows.UI.Xaml.IUIElement10,
                   ctyped.interface.Windows.UI.Xaml.IUIElementOverrides,
                   ctyped.interface.Windows.UI.Xaml.IUIElementOverrides7,
                   ctyped.interface.Windows.UI.Xaml.IUIElementOverrides8,
                   ctyped.interface.Windows.UI.Xaml.IUIElementOverrides9)

    @classmethod
    @property
    def allow_drop_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_AllowDropProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def opacity_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_OpacityProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def clip_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_ClipProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def render_transform_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_RenderTransformProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def projection_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_ProjectionProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def render_transform_origin_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_RenderTransformOriginProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_hit_test_visible_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_IsHitTestVisibleProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def visibility_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_VisibilityProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def use_layout_rounding_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_UseLayoutRoundingProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def transitions_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_TransitionsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def cache_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_CacheModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_tap_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_IsTapEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_double_tap_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_IsDoubleTapEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_right_tap_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_IsRightTapEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_holding_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_IsHoldingEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def manipulation_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_ManipulationModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def pointer_captures_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics].get_PointerCapturesProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def shadow_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics10].get_ShadowProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def composite_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics2].get_CompositeModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def transform_3d_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics3].get_Transform3DProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def can_drag_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics3].get_CanDragProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def context_flyout_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics4].get_ContextFlyoutProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def exit_display_mode_on_access_key_invoked_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics4].get_ExitDisplayModeOnAccessKeyInvokedProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_access_key_scope_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics4].get_IsAccessKeyScopeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def access_key_scope_owner_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics4].get_AccessKeyScopeOwnerProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def access_key_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics4].get_AccessKeyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def lights_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_LightsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_placement_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipPlacementModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_horizontal_offset_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipHorizontalOffsetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_vertical_offset_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_KeyTipVerticalOffsetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_keyboard_navigation_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusKeyboardNavigationProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_up_navigation_strategy_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusUpNavigationStrategyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_down_navigation_strategy_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusDownNavigationStrategyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_left_navigation_strategy_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusLeftNavigationStrategyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_right_navigation_strategy_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_XYFocusRightNavigationStrategyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def high_contrast_adjustment_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_HighContrastAdjustmentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def tab_focus_navigation_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics5].get_TabFocusNavigationProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def key_tip_target_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyTipTargetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_placement_target_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyboardAcceleratorPlacementTargetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_placement_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics8].get_KeyboardAcceleratorPlacementModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def can_be_scroll_anchor_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IUIElementStatics9].get_CanBeScrollAnchorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def desired_size(self) -> ctyped.struct.Windows.Foundation.Size:
        value = ctyped.struct.Windows.Foundation.Size()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_DesiredSize(ctyped.byref(value))
        return value

    @property
    def allow_drop(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_AllowDrop(ctyped.byref(value))
        return value

    @allow_drop.setter
    def allow_drop(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_AllowDrop(value)

    @property
    def opacity(self) -> ctyped.type.DOUBLE:
        value = ctyped.type.DOUBLE()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_Opacity(ctyped.byref(value))
        return value

    @opacity.setter
    def opacity(self, value: ctyped.type.DOUBLE):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_Opacity(value)

    @property
    def visibility(self) -> ctyped.enum.Windows.UI.Xaml.Visibility:
        value = ctyped.enum.Windows.UI.Xaml.Visibility()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_Visibility(ctyped.byref(value))
        return value

    @visibility.setter
    def visibility(self, value: ctyped.enum.Windows.UI.Xaml.Visibility):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_Visibility(value)

    @property
    def render_size(self) -> ctyped.struct.Windows.Foundation.Size:
        value = ctyped.struct.Windows.Foundation.Size()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_RenderSize(ctyped.byref(value))
        return value

    @property
    def use_layout_rendering(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_UseLayoutRounding(ctyped.byref(value))
        return value

    @use_layout_rendering.setter
    def use_layout_rendering(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_UseLayoutRounding(value)

    @property
    def is_tap_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_IsTapEnabled(ctyped.byref(value))
        return value

    @is_tap_enabled.setter
    def is_tap_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_IsTapEnabled(value)

    @property
    def is_double_tap_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_IsDoubleTapEnabled(ctyped.byref(value))
        return value

    @is_double_tap_enabled.setter
    def is_double_tap_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_IsDoubleTapEnabled(value)

    @property
    def is_right_tap_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_IsRightTapEnabled(ctyped.byref(value))
        return value

    @is_right_tap_enabled.setter
    def is_right_tap_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_IsRightTapEnabled(value)

    @property
    def is_holding_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].get_IsHoldingEnabled(ctyped.byref(value))
        return value

    @is_holding_enabled.setter
    def is_holding_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.IUIElement].put_IsHoldingEnabled(value)

    def measure(self, available_size: ctyped.struct.Windows.Foundation.Size) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IUIElement].Measure(available_size))

    def arrange(self, final_size: ctyped.struct.Windows.Foundation.Rect) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IUIElement].Arrange(final_size))

    def invalidate_measure(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IUIElement].InvalidateMeasure())

    def invalidate_arrange(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IUIElement].InvalidateArrange())

    def update_layout(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IUIElement].UpdateLayout())


class FrameworkElement(UIElement):
    _statics = (ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics,
                ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics2,
                ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4,
                ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics5,
                ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics6)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IFrameworkElement,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElement2,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElement3,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElement4,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElement6,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElement7,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElementProtected7,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElementOverrides,
                   ctyped.interface.Windows.UI.Xaml.IFrameworkElementOverrides2)

    @classmethod
    @property
    def tag_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_TagProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def language_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_LanguageProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def actual_width_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_ActualWidthProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def actual_height_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_ActualHeightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def width_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_WidthProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def height_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_HeightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def min_width_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MinWidthProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def max_width_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MaxWidthProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def min_height_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MinHeightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def max_height_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MaxHeightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def horizontal_alignment_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_HorizontalAlignmentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def vertical_alignment_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_VerticalAlignmentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def margin_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_MarginProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def name_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_NameProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def data_context_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_DataContextProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def style_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_StyleProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def flow_direction_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics].get_FlowDirectionProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def requested_theme_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics2].get_RequestedThemeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_on_interaction_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_AllowFocusOnInteractionProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_margin_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualMarginProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_secondary_thickness_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualSecondaryThicknessProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_primary_thickness_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualPrimaryThicknessProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_secondary_brush_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualSecondaryBrushProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_visual_primary_brush_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_FocusVisualPrimaryBrushProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_when_disabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics4].get_AllowFocusWhenDisabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def actual_theme_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IFrameworkElementStatics6].get_ActualThemeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def tag(self) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].get_Tag(ctyped.byref(obj))
            return Inspectable(obj)

    @tag.setter
    def tag(self, value: Inspectable):
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].put_Tag(value[ctyped.interface.IInspectable])

    @property
    def language(self) -> ctyped.handle.HSTRING:
        value = ctyped.handle.HSTRING()
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].get_Language(ctyped.byref(value))
        return value

    @language.setter
    def language(self, value: ctyped.handle.HSTRING):
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].put_Language(value)

    @property
    def horizontal_alignment(self) -> ctyped.enum.Windows.UI.Xaml.HorizontalAlignment:
        value = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment()
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].get_HorizontalAlignment(ctyped.byref(value))
        return value

    @horizontal_alignment.setter
    def horizontal_alignment(self, value: ctyped.enum.Windows.UI.Xaml.HorizontalAlignment):
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].put_HorizontalAlignment(value)

    @property
    def vertical_alignment(self) -> ctyped.enum.Windows.UI.Xaml.VerticalAlignment:
        value = ctyped.enum.Windows.UI.Xaml.VerticalAlignment()
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].get_VerticalAlignment(ctyped.byref(value))
        return value

    @vertical_alignment.setter
    def vertical_alignment(self, value: ctyped.enum.Windows.UI.Xaml.VerticalAlignment):
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement].put_VerticalAlignment(value)

    @property
    def requested_theme(self) -> ctyped.enum.Windows.UI.Xaml.ElementTheme:
        value = ctyped.enum.Windows.UI.Xaml.ElementTheme()
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement2].get_RequestedTheme(ctyped.byref(value))
        return value

    @requested_theme.setter
    def requested_theme(self, value: ctyped.enum.Windows.UI.Xaml.ElementTheme):
        self[ctyped.interface.Windows.UI.Xaml.IFrameworkElement2].put_RequestedTheme(value)


class Control(FrameworkElement):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IControlFactory,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics2,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics3,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics5,
                ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics7)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IControl,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControl2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControl3,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControl4,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControl5,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControl7,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControlProtected,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControlOverrides,
                   ctyped.interface.Windows.UI.Xaml.Controls.IControlOverrides6)

    @classmethod
    @property
    def font_size_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontSizeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def font_family_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontFamilyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def font_weight_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontWeightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def font_style_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontStyleProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def font_stretch_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FontStretchProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def character_spacing_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_CharacterSpacingProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def foreground_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_ForegroundProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_tab_stop_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_IsTabStopProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_IsEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def tab_index_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_TabIndexProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def tab_navigation_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_TabNavigationProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def template_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_TemplateProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def padding_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_PaddingProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def horizontal_content_alignment_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_HorizontalContentAlignmentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def vertical_content_alignment_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_VerticalContentAlignmentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def background_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_BackgroundProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def border_thickness_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_BorderThicknessProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def border_brush_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_BorderBrushProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def default_style_key_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_DefaultStyleKeyProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def focus_state_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics].get_FocusStateProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_text_scale_factor_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics2].get_IsTextScaleFactorEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def use_system_focus_visuals_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics3].get_UseSystemFocusVisualsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_template_focus_target_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics3].get_IsTemplateFocusTargetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_focus_engagement_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_IsFocusEngagementEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_focus_engaged_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_IsFocusEngagedProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def requires_pointer_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_RequiresPointerProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_left_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusLeftProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_right_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusRightProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_up_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusUpProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def xy_focus_down_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_XYFocusDownProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def element_sound_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics4].get_ElementSoundModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def default_style_resource_uri_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics5].get_DefaultStyleResourceUriProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_template_key_tip_target_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics5].get_IsTemplateKeyTipTargetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def background_sizing_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics7].get_BackgroundSizingProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def corner_radius_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IControlStatics7].get_CornerRadiusProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def font_size(self) -> ctyped.type.DOUBLE:
        value = ctyped.type.DOUBLE()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl].get_FontSize(ctyped.byref(value))
        return value

    @font_size.setter
    def font_size(self, value: ctyped.type.DOUBLE):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl].put_FontSize(value)

    @property
    def background(self) -> Brush:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.Media.IBrush, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.IControl].get_Background(ctyped.byref(obj))
            return Brush(obj)

    @background.setter
    def background(self, value: Brush):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl].put_Background(value[ctyped.interface.Windows.UI.Xaml.Media.IBrush])

    @property
    def background_sizing(self) -> ctyped.enum.Windows.UI.Xaml.Controls.BackgroundSizing:
        value = ctyped.enum.Windows.UI.Xaml.Controls.BackgroundSizing()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl7].get_BackgroundSizing(ctyped.byref(value))
        return value

    @background_sizing.setter
    def background_sizing(self, value: ctyped.enum.Windows.UI.Xaml.Controls.BackgroundSizing):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl7].put_BackgroundSizing(value)

    @property
    def corner_radius(self) -> ctyped.struct.Windows.UI.Xaml.CornerRadius:
        value = ctyped.struct.Windows.UI.Xaml.CornerRadius()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl7].get_CornerRadius(ctyped.byref(value))
        return value

    @corner_radius.setter
    def corner_radius(self, value: ctyped.struct.Windows.UI.Xaml.CornerRadius):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IControl7].put_CornerRadius(value)


class ContentControl(Control):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IContentControlStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IContentControl,
                   ctyped.interface.Windows.UI.Xaml.Controls.IContentControl2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IContentControlOverrides)

    @classmethod
    @property
    def content_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def content_template_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTemplateProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def content_template_selector_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTemplateSelectorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def content_transitions_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IContentControlStatics].get_ContentTransitionsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def content(self) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.IContentControl].get_Content(ctyped.byref(obj))
            return Inspectable(obj)

    @content.setter
    def content(self, value: Inspectable):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IContentControl].put_Content(value[ctyped.interface.IInspectable])


class ButtonBase(ContentControl):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBase,)

    @classmethod
    @property
    def click_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_ClickModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_pointer_over_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_IsPointerOverProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_pressed_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_IsPressedProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def command_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_CommandProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def command_parameter_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IButtonBaseStatics].get_CommandParameterProperty(ctyped.byref(obj))
            return DependencyProperty(obj)


class Button(ButtonBase):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IButtonStaticsWithFlyout,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IButton,
                   ctyped.interface.Windows.UI.Xaml.Controls.IButtonWithFlyout)

    @classmethod
    @property
    def flyout_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IButtonStaticsWithFlyout].get_FlyoutProperty(ctyped.byref(obj))
            return DependencyProperty(obj)


class DropDownButton(Button):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IDropDownButton,)


class Brush(AnimationObject, DependencyObject):
    _statics = (ctyped.interface.Windows.UI.Xaml.Media.IBrushStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Media.IBrush,
                   ctyped.interface.Windows.UI.Xaml.Media.IBrushOverrides2)


class SolidColorBrush(Brush):
    _statics = (ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrushFactory,
                ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrushStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrush,)

    @classmethod
    def create_instance_with_color(cls, color: ctyped.struct.Windows.UI.Color) -> SolidColorBrush:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrush, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrushFactory].CreateInstanceWithColor(color, ctyped.byref(obj))
            return SolidColorBrush(obj)

    @classmethod
    @property
    def color_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrushStatics].get_ColorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def color(self) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        self[ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrush].get_Color(ctyped.byref(value))
        return value

    @color.setter
    def color(self, value: ctyped.struct.Windows.UI.Color):
        self[ctyped.interface.Windows.UI.Xaml.Media.ISolidColorBrush].put_Color(value)


class Panel(FrameworkElement):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IPanelStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IPanel,
                   ctyped.interface.Windows.UI.Xaml.Controls.IPanel2)

    @property
    def children(self) -> UIElementCollection:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.IUIElement], False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.IPanel].get_Children(ctyped.byref(obj))
            return UIElementCollection(obj)


class StackPanel(ScrollSnapPointsInfo, InsertionPanel, Panel):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IStackPanelStatics,
                ctyped.interface.Windows.UI.Xaml.Controls.IStackPanelStatics2,
                ctyped.interface.Windows.UI.Xaml.Controls.IStackPanelStatics4,
                ctyped.interface.Windows.UI.Xaml.Controls.IStackPanelStatics5)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IStackPanel,
                   ctyped.interface.Windows.UI.Xaml.Controls.IStackPanel2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IStackPanel4,
                   ctyped.interface.Windows.UI.Xaml.Controls.IStackPanel5)


class TextBlock(FrameworkElement):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics,
                ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics2,
                ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics3,
                ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics5,
                ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics6,
                ctyped.interface.Windows.UI.Xaml.Controls.ITextBlockStatics7)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock2,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock3,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock4,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock5,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock6,
                   ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock7)

    @property
    def font_size(self) -> ctyped.type.DOUBLE:
        value = ctyped.type.DOUBLE()
        self[ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock].get_FontSize(ctyped.byref(value))
        return value

    @font_size.setter
    def font_size(self, value: ctyped.type.DOUBLE):
        self[ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock].put_FontSize(value)

    @property
    def text(self) -> ctyped.handle.HSTRING:
        value = ctyped.handle.HSTRING()
        self[ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock].get_Text(ctyped.byref(value))
        return value

    @text.setter
    def text(self, value: ctyped.handle.HSTRING):
        self[ctyped.interface.Windows.UI.Xaml.Controls.ITextBlock].put_Text(value)


class PropertyValue(Inspectable):
    _statics = (ctyped.interface.Windows.Foundation.IPropertyValueStatics,)
    _interfaces = (ctyped.interface.Windows.Foundation.IPropertyValue,)

    @classmethod
    def create_empty(cls) -> PropertyValue:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.IPropertyValue, False) as obj:
            cls[ctyped.interface.Windows.Foundation.IPropertyValueStatics].CreateEmpty(ctyped.byref(obj))
            return PropertyValue(obj)

    @classmethod
    def create_uint8(cls, value: ctyped.type.BYTE) -> PropertyValue:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.IPropertyValue, False) as obj:
            cls[ctyped.interface.Windows.Foundation.IPropertyValueStatics].CreateUInt8(value, ctyped.byref(obj))
            return PropertyValue(obj)

    @classmethod
    def create_int16(cls, value: ctyped.type.SHORT) -> PropertyValue:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.IPropertyValue, False) as obj:
            cls[ctyped.interface.Windows.Foundation.IPropertyValueStatics].CreateInt16(value, ctyped.byref(obj))
            return PropertyValue(obj)

    @classmethod
    def create_boolean(cls, value: bool) -> PropertyValue:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.IPropertyValue, False) as obj:
            cls[ctyped.interface.Windows.Foundation.IPropertyValueStatics].CreateBoolean(value, ctyped.byref(obj))
            return PropertyValue(obj)

    @classmethod
    def create_string(cls, value: ctyped.handle.HSTRING) -> PropertyValue:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            cls[ctyped.interface.Windows.Foundation.IPropertyValueStatics].CreateString(value, ctyped.byref(obj))
            return PropertyValue(obj)


class Colors(Inspectable):
    _statics = (ctyped.interface.Windows.UI.IColorsStatics,)

    @classmethod
    @property
    def alice_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_AliceBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def antique_white(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_AntiqueWhite(ctyped.byref(value))
        return value

    @classmethod
    @property
    def aqua(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Aqua(ctyped.byref(value))
        return value

    @classmethod
    @property
    def aquamarine(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Aquamarine(ctyped.byref(value))
        return value

    @classmethod
    @property
    def azure(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Azure(ctyped.byref(value))
        return value

    @classmethod
    @property
    def beige(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Beige(ctyped.byref(value))
        return value

    @classmethod
    @property
    def bisque(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Bisque(ctyped.byref(value))
        return value

    @classmethod
    @property
    def black(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Black(ctyped.byref(value))
        return value

    @classmethod
    @property
    def blanched_almond(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_BlanchedAlmond(ctyped.byref(value))
        return value

    @classmethod
    @property
    def blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Blue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def blue_violet(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_BlueViolet(ctyped.byref(value))
        return value

    @classmethod
    @property
    def brown(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Brown(ctyped.byref(value))
        return value

    @classmethod
    @property
    def burly_wood(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_BurlyWood(ctyped.byref(value))
        return value

    @classmethod
    @property
    def cadet_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_CadetBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def chartreuse(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Chartreuse(ctyped.byref(value))
        return value

    @classmethod
    @property
    def chocolate(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Chocolate(ctyped.byref(value))
        return value

    @classmethod
    @property
    def coral(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Coral(ctyped.byref(value))
        return value

    @classmethod
    @property
    def cornflower_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_CornflowerBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def cornsilk(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Cornsilk(ctyped.byref(value))
        return value

    @classmethod
    @property
    def crimson(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Crimson(ctyped.byref(value))
        return value

    @classmethod
    @property
    def cyan(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Cyan(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_cyan(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkCyan(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_goldenrod(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkGoldenrod(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_khaki(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkKhaki(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_magenta(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkMagenta(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_olive_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkOliveGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_orange(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkOrange(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_orchid(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkOrchid(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkRed(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_salmon(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkSalmon(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_sea_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkSeaGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_slate_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkSlateBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_slate_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkSlateGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_turquoise(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkTurquoise(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dark_violet(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DarkViolet(ctyped.byref(value))
        return value

    @classmethod
    @property
    def deep_pink(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DeepPink(ctyped.byref(value))
        return value

    @classmethod
    @property
    def deep_sky_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DeepSkyBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dim_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DimGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def dodger_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_DodgerBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def firebrick(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Firebrick(ctyped.byref(value))
        return value

    @classmethod
    @property
    def floral_white(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_FloralWhite(ctyped.byref(value))
        return value

    @classmethod
    @property
    def forest_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_ForestGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def fuchsia(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Fuchsia(ctyped.byref(value))
        return value

    @classmethod
    @property
    def gainsboro(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Gainsboro(ctyped.byref(value))
        return value

    @classmethod
    @property
    def ghost_white(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_GhostWhite(ctyped.byref(value))
        return value

    @classmethod
    @property
    def gold(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Gold(ctyped.byref(value))
        return value

    @classmethod
    @property
    def goldenrod(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Goldenrod(ctyped.byref(value))
        return value

    @classmethod
    @property
    def gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Gray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Green(ctyped.byref(value))
        return value

    @classmethod
    @property
    def green_yellow(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_GreenYellow(ctyped.byref(value))
        return value

    @classmethod
    @property
    def honeydew(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Honeydew(ctyped.byref(value))
        return value

    @classmethod
    @property
    def hot_pink(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_HotPink(ctyped.byref(value))
        return value

    @classmethod
    @property
    def indian_red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_IndianRed(ctyped.byref(value))
        return value

    @classmethod
    @property
    def indigo(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Indigo(ctyped.byref(value))
        return value

    @classmethod
    @property
    def ivory(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Ivory(ctyped.byref(value))
        return value

    @classmethod
    @property
    def khaki(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Khaki(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lavender(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Lavender(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lavender_blush(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LavenderBlush(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lawn_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LawnGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lemon_chiffon(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LemonChiffon(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_coral(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightCoral(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_cyan(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightCyan(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_goldenrod_yellow(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightGoldenrodYellow(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_pink(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightPink(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_salmon(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightSalmon(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_sea_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightSeaGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_sky_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightSkyBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_slate_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightSlateGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_steel_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightSteelBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def light_yellow(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LightYellow(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lime(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Lime(ctyped.byref(value))
        return value

    @classmethod
    @property
    def lime_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_LimeGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def linen(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Linen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def magenta(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Magenta(ctyped.byref(value))
        return value

    @classmethod
    @property
    def maroon(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Maroon(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_aquamarine(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumAquamarine(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_orchid(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumOrchid(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_purple(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumPurple(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_sea_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumSeaGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_slate_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumSlateBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_spring_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumSpringGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_turquoise(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumTurquoise(ctyped.byref(value))
        return value

    @classmethod
    @property
    def medium_violet_red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MediumVioletRed(ctyped.byref(value))
        return value

    @classmethod
    @property
    def midnight_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MidnightBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def mint_cream(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MintCream(ctyped.byref(value))
        return value

    @classmethod
    @property
    def misty_rose(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_MistyRose(ctyped.byref(value))
        return value

    @classmethod
    @property
    def moccasin(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Moccasin(ctyped.byref(value))
        return value

    @classmethod
    @property
    def navajo_white(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_NavajoWhite(ctyped.byref(value))
        return value

    @classmethod
    @property
    def navy(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Navy(ctyped.byref(value))
        return value

    @classmethod
    @property
    def old_lace(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_OldLace(ctyped.byref(value))
        return value

    @classmethod
    @property
    def olive(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Olive(ctyped.byref(value))
        return value

    @classmethod
    @property
    def olive_drab(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_OliveDrab(ctyped.byref(value))
        return value

    @classmethod
    @property
    def orange(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Orange(ctyped.byref(value))
        return value

    @classmethod
    @property
    def orange_red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_OrangeRed(ctyped.byref(value))
        return value

    @classmethod
    @property
    def orchid(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Orchid(ctyped.byref(value))
        return value

    @classmethod
    @property
    def pale_goldenrod(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PaleGoldenrod(ctyped.byref(value))
        return value

    @classmethod
    @property
    def pale_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PaleGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def pale_turquoise(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PaleTurquoise(ctyped.byref(value))
        return value

    @classmethod
    @property
    def pale_violet_red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PaleVioletRed(ctyped.byref(value))
        return value

    @classmethod
    @property
    def papaya_whip(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PapayaWhip(ctyped.byref(value))
        return value

    @classmethod
    @property
    def peach_puff(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PeachPuff(ctyped.byref(value))
        return value

    @classmethod
    @property
    def peru(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Peru(ctyped.byref(value))
        return value

    @classmethod
    @property
    def pink(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Pink(ctyped.byref(value))
        return value

    @classmethod
    @property
    def plum(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Plum(ctyped.byref(value))
        return value

    @classmethod
    @property
    def powder_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_PowderBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def purple(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Purple(ctyped.byref(value))
        return value

    @classmethod
    @property
    def red(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Red(ctyped.byref(value))
        return value

    @classmethod
    @property
    def rosy_brown(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_RosyBrown(ctyped.byref(value))
        return value

    @classmethod
    @property
    def royal_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_RoyalBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def saddle_brown(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SaddleBrown(ctyped.byref(value))
        return value

    @classmethod
    @property
    def salmon(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Salmon(ctyped.byref(value))
        return value

    @classmethod
    @property
    def sandy_brown(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SandyBrown(ctyped.byref(value))
        return value

    @classmethod
    @property
    def sea_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SeaGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def sea_shell(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SeaShell(ctyped.byref(value))
        return value

    @classmethod
    @property
    def sienna(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Sienna(ctyped.byref(value))
        return value

    @classmethod
    @property
    def silver(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Silver(ctyped.byref(value))
        return value

    @classmethod
    @property
    def sky_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SkyBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def slate_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SlateBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def slate_gray(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SlateGray(ctyped.byref(value))
        return value

    @classmethod
    @property
    def snow(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Snow(ctyped.byref(value))
        return value

    @classmethod
    @property
    def spring_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SpringGreen(ctyped.byref(value))
        return value

    @classmethod
    @property
    def steel_blue(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_SteelBlue(ctyped.byref(value))
        return value

    @classmethod
    @property
    def tan(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Tan(ctyped.byref(value))
        return value

    @classmethod
    @property
    def teal(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Teal(ctyped.byref(value))
        return value

    @classmethod
    @property
    def thistle(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Thistle(ctyped.byref(value))
        return value

    @classmethod
    @property
    def tomato(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Tomato(ctyped.byref(value))
        return value

    @classmethod
    @property
    def transparent(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Transparent(ctyped.byref(value))
        return value

    @classmethod
    @property
    def turquoise(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Turquoise(ctyped.byref(value))
        return value

    @classmethod
    @property
    def violet(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Violet(ctyped.byref(value))
        return value

    @classmethod
    @property
    def wheat(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Wheat(ctyped.byref(value))
        return value

    @classmethod
    @property
    def white(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_White(ctyped.byref(value))
        return value

    @classmethod
    @property
    def white_smoke(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_WhiteSmoke(ctyped.byref(value))
        return value

    @classmethod
    @property
    def yellow(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_Yellow(ctyped.byref(value))
        return value

    @classmethod
    @property
    def yellow_green(cls) -> ctyped.struct.Windows.UI.Color:
        value = ctyped.struct.Windows.UI.Color()
        cls[ctyped.interface.Windows.UI.IColorsStatics].get_YellowGreen(ctyped.byref(value))
        return value


class XamlReader(Inspectable):
    _statics = (ctyped.interface.Windows.UI.Xaml.Markup.IXamlReaderStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Markup.IXamlReader,)

    @classmethod
    def load(cls, xaml: ctyped.handle.HSTRING) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Markup.IXamlReaderStatics].Load(xaml, ctyped.byref(obj))
            return Inspectable(obj)

    @classmethod
    def load_with_initial_template_validation(cls, xaml: ctyped.handle.HSTRING) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Markup.IXamlReaderStatics].LoadWithInitialTemplateValidation(xaml, ctyped.byref(obj))
            return Inspectable(obj)


class SetterBase(DependencyObject):
    _statics = (ctyped.interface.Windows.UI.Xaml.ISetterBaseFactory,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.ISetterBase,)

    @property
    def is_sealed(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.ISetterBase].get_IsSealed(ctyped.byref(value))
        return value


class _IIterator(Inspectable):
    _t_iterator: tuple[type[ctyped.interface.IInspectable], _Optional[type[Inspectable]]]

    @property
    def current(self):
        with ctyped.init_com(self._t_iterator[0], False) as obj:
            self[ctyped.interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].get_Current(ctyped.byref(obj))
            return obj if self._t_iterator[1] is None else self._t_iterator[1](obj)

    @property
    def has_current(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].get_HasCurrent(ctyped.byref(value))
        return value

    def move_next(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.Foundation.Collections.IIterator[self._t_iterator[0]]].MoveNext(ctyped.byref(value))
        return value


class IteratorSetterBase(_IIterator):
    _t_iterator = (ctyped.interface.Windows.UI.Xaml.ISetterBase, SetterBase)
    _interfaces = (ctyped.interface.Windows.Foundation.Collections.IIterator[ctyped.interface.Windows.UI.Xaml.ISetterBase],)

    current: SetterBase


class _IIterable(Inspectable):
    _t_iterable: tuple[type[ctyped.interface.IInspectable], _Optional[type[Inspectable]]]

    def first(self):
        with ctyped.init_com(ctyped.interface.Windows.Foundation.Collections.IIterator[self._t_iterable[0]], False) as obj:
            self[ctyped.interface.Windows.Foundation.Collections.IIterable[self._t_iterable[0]]].First(ctyped.byref(obj))
            return obj if self._t_iterable[1] is None else self._t_iterable[1](obj)


class IterableSetterBase(_IIterable):
    _t_iterable = (ctyped.interface.Windows.UI.Xaml.ISetterBase, IteratorSetterBase)
    _interfaces = (ctyped.interface.Windows.Foundation.Collections.IIterable[ctyped.interface.Windows.UI.Xaml.ISetterBase],)

    first: _Callable[[], IteratorSetterBase]


class _IVector(Inspectable):
    _t_vector: tuple[type[ctyped.interface.IInspectable], _Optional[type[Inspectable]]]

    def get_at(self, index: ctyped.type.c_uint):
        with ctyped.init_com(self._t_vector[0], False) as obj:
            self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].GetAt(index, ctyped.byref(obj))
            return obj if self._t_vector[1] is None else self._t_vector[1](obj)

    @property
    def size(self) -> ctyped.type.c_uint:
        value = ctyped.type.c_uint()
        self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].get_Size(ctyped.byref(value))
        return value

    def set_at(self, index: ctyped.type.c_uint, value) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].SetAt(index, value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def insert_at(self, index: ctyped.type.c_uint, value) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].InsertAt(index, value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def remove_at(self, index: ctyped.type.c_uint) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].RemoveAt(index))

    def append(self, value) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].Append(value if self._t_vector[1] is None else value[self._t_vector[0]]))

    def remove_at_end(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].RemoveAtEnd())

    def clear(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.Foundation.Collections.IVector[self._t_vector[0]]].Clear())


class DependencyProperty(Inspectable):
    _statics = (ctyped.interface.Windows.UI.Xaml.IDependencyPropertyStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IDependencyProperty,)

    @classmethod
    def unset_value(cls) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IDependencyPropertyStatics].UnsetValue(ctyped.byref(obj))
            return Inspectable(obj)


class Setter(SetterBase):
    _statics = (ctyped.interface.Windows.UI.Xaml.ISetterFactory,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.ISetter,
                   ctyped.interface.Windows.UI.Xaml.ISetter2,)

    @classmethod
    def create_instance(cls, target_property: DependencyProperty, value: Inspectable) -> Setter:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.ISetter, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.ISetterFactory].CreateInstance(target_property[ctyped.interface.Windows.UI.Xaml.IDependencyProperty], value[ctyped.interface.IInspectable], ctyped.byref(obj))
            return Setter(obj)

    @property
    def property(self) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.ISetter].get_Property(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property.setter
    def property(self, value: DependencyProperty):
        self[ctyped.interface.Windows.UI.Xaml.ISetter].put_Property(value[ctyped.interface.Windows.UI.Xaml.IDependencyProperty])

    @_builtins.property
    def value(self) -> Inspectable:
        with ctyped.init_com(ctyped.interface.IInspectable, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.ISetter].get_Value(ctyped.byref(obj))
            return Inspectable(obj)

    # noinspection PyUnresolvedReferences
    @value.setter
    def value(self, value: Inspectable):
        self[ctyped.interface.Windows.UI.Xaml.ISetter].put_Value(value[ctyped.interface.IInspectable])


class MenuFlyoutItemBase(Control):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBaseFactory,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase,)


class VectorUIElement(_IVector):
    _t_vector = (ctyped.interface.Windows.UI.Xaml.IUIElement, UIElement)
    _interfaces = (ctyped.interface.Windows.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.IUIElement],)

    get_at: _Callable[[ctyped.type.c_uint], UIElement]
    set_at: _Callable[[ctyped.type.c_uint, UIElement], bool]
    insert_at: _Callable[[ctyped.type.c_uint, UIElement], bool]
    append: _Callable[[UIElement], bool]


class VectorSetterBase(_IVector):
    _t_vector = (ctyped.interface.Windows.UI.Xaml.ISetterBase, SetterBase)
    _interfaces = (ctyped.interface.Windows.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.ISetterBase],)

    get_at: _Callable[[ctyped.type.c_uint], SetterBase]
    set_at: _Callable[[ctyped.type.c_uint, SetterBase], bool]
    insert_at: _Callable[[ctyped.type.c_uint, SetterBase], bool]
    append: _Callable[[SetterBase], bool]


class VectorMenuFlyoutItemBase(_IVector):
    _t_vector = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase, MenuFlyoutItemBase)
    _interfaces = (ctyped.interface.Windows.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase],)

    get_at: _Callable[[ctyped.type.c_uint], MenuFlyoutItemBase]
    set_at: _Callable[[ctyped.type.c_uint, MenuFlyoutItemBase], bool]
    insert_at: _Callable[[ctyped.type.c_uint, MenuFlyoutItemBase], bool]
    append: _Callable[[MenuFlyoutItemBase], bool]


class UIElementCollection(VectorUIElement):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IUIElementCollection,)


class SetterBaseCollection(IterableSetterBase, VectorSetterBase):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.ISetterBaseCollection,)

    @property
    def is_sealed(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.ISetterBase].get_IsSealed(ctyped.byref(value))
        return value


class FlyoutBase(DependencyObject):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics,
                ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2,
                ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3,
                ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5,
                ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase4,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides,
                   ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseOverrides4)

    @classmethod
    @property
    def placement_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].get_PlacementProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def attached_flyout_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].get_AttachedFlyoutProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    def get_attached_flyout(cls, element: FrameworkElement) -> FlyoutBase:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].GetAttachedFlyout(element[ctyped.interface.Windows.UI.Xaml.IFrameworkElement], ctyped.byref(obj))
            return FlyoutBase(obj)

    @classmethod
    def set_attached_flyout(cls, element: FrameworkElement, value: FlyoutBase) -> bool:
        return ctyped.macro.SUCCEEDED(cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].SetAttachedFlyout(
            element[ctyped.interface.Windows.UI.Xaml.IFrameworkElement], value[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase]))

    @classmethod
    def show_attached_flyout(cls, element: FrameworkElement) -> bool:
        return ctyped.macro.SUCCEEDED(cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics].ShowAttachedFlyout(element[ctyped.interface.Windows.UI.Xaml.IFrameworkElement]))

    @classmethod
    @property
    def allow_focus_on_interaction_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_AllowFocusOnInteractionProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def light_dismiss_overlay_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_LightDismissOverlayModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def allow_focus_when_disabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_AllowFocusWhenDisabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def element_sound_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics2].get_ElementSoundModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def overlay_input_pass_through_element_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics3].get_OverlayInputPassThroughElementProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def target_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_TargetProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def show_mode_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_ShowModeProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def input_device_prefers_primary_commands_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_InputDevicePrefersPrimaryCommandsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def are_open_close_animations_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_AreOpenCloseAnimationsEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_open_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics5].get_IsOpenProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def should_constrain_to_root_bounds_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseStatics6].get_ShouldConstrainToRootBoundsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def placement(self) -> ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode:
        value = ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].get_Placement(ctyped.byref(value))
        return value

    @placement.setter
    def placement(self, value: ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].put_Placement(value)

    def show_at(self, placement_target: FrameworkElement) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].ShowAt(placement_target[ctyped.interface.Windows.UI.Xaml.IFrameworkElement]))

    def hide(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase].Hide())

    @property
    def target(self) -> FrameworkElement:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IFrameworkElement, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_Target(ctyped.byref(obj))
            return FrameworkElement(obj)

    @property
    def allow_focus_on_interaction(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_AllowFocusOnInteraction(ctyped.byref(value))
        return value

    @allow_focus_on_interaction.setter
    def allow_focus_on_interaction(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_AllowFocusOnInteraction(value)

    @property
    def light_dismiss_overlay_mode(self) -> ctyped.enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode:
        value = ctyped.enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_LightDismissOverlayMode(ctyped.byref(value))
        return value

    @light_dismiss_overlay_mode.setter
    def light_dismiss_overlay_mode(self, value: ctyped.enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_LightDismissOverlayMode(value)

    @property
    def allow_focus_when_disabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_AllowFocusWhenDisabled(ctyped.byref(value))
        return value

    @allow_focus_when_disabled.setter
    def allow_focus_when_disabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_AllowFocusWhenDisabled(value)

    @property
    def element_sound_mode(self) -> ctyped.enum.Windows.UI.Xaml.ElementSoundMode:
        value = ctyped.enum.Windows.UI.Xaml.ElementSoundMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].get_ElementSoundMode(ctyped.byref(value))
        return value

    @element_sound_mode.setter
    def element_sound_mode(self, value: ctyped.enum.Windows.UI.Xaml.ElementSoundMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase2].put_ElementSoundMode(value)

    @property
    def overlay_input_pass_through_element(self) -> DependencyObject:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyObject, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3].get_OverlayInputPassThroughElement(ctyped.byref(obj))
            return DependencyObject(obj)

    @overlay_input_pass_through_element.setter
    def overlay_input_pass_through_element(self, value: DependencyObject):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase3].put_OverlayInputPassThroughElement(value[ctyped.interface.Windows.UI.Xaml.IDependencyObject])

    @property
    def show_mode(self) -> ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode:
        value = ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_ShowMode(ctyped.byref(value))
        return value

    @show_mode.setter
    def show_mode(self, value: ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].put_ShowMode(value)

    @property
    def input_device_prefers_primary_commands(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_InputDevicePrefersPrimaryCommands(ctyped.byref(value))
        return value

    @property
    def are_open_close_animations_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_AreOpenCloseAnimationsEnabled(ctyped.byref(value))
        return value

    @are_open_close_animations_enabled.setter
    def are_open_close_animations_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].put_AreOpenCloseAnimationsEnabled(value)

    @property
    def is_open(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].get_IsOpen(ctyped.byref(value))
        return value

    def show_at_(self, placement_target: DependencyObject, show_options: FlyoutShowOptions) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase5].ShowAt(
            placement_target[ctyped.interface.Windows.UI.Xaml.IDependencyObject], show_options[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions]))

    @property
    def should_constrain_to_root_bounds(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].get_ShouldConstrainToRootBounds(ctyped.byref(value))
        return value

    @should_constrain_to_root_bounds.setter
    def should_constrain_to_root_bounds(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].put_ShouldConstrainToRootBounds(value)

    @property
    def is_constrained_to_root_bounds(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutBase6].get_IsConstrainedToRootBounds(ctyped.byref(value))
        return value


class FlyoutShowOptions(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions,)

    @property
    def show_mode(self) -> ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode:
        value = ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].get_ShowMode(ctyped.byref(value))
        return value

    @show_mode.setter
    def show_mode(self, value: ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].put_ShowMode(value)

    @property
    def placement(self) -> ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode:
        value = ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode()
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].get_Placement(ctyped.byref(value))
        return value

    @placement.setter
    def placement(self, value: ctyped.enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode):
        self[ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions].put_Placement(value)


class ItemContainerMapping(Inspectable):
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IItemContainerMapping,)


class ItemsControl(ItemContainerMapping, Control):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlFactory,
                ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IItemsControl,
                   ctyped.interface.Windows.UI.Xaml.Controls.IItemsControl2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IItemsControl3,
                   ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlOverrides)

    @classmethod
    @property
    def items_source_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemsSourceProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def item_template_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemTemplateProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def item_template_selector_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemTemplateSelectorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def items_panel_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemsPanelProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def display_member_path_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_DisplayMemberPathProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_style_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerStyleProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_style_selector_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerStyleSelectorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def item_container_transitions_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_ItemContainerTransitionsProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def group_style_selector_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_GroupStyleSelectorProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def is_grouping_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IItemsControlStatics].get_IsGroupingProperty(ctyped.byref(obj))
            return DependencyProperty(obj)


class MenuFlyoutPresenter(ItemsControl):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterFactory,
                ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterStatics3)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter,
                   ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3)

    @classmethod
    @property
    def is_default_shadow_enabled_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenterStatics3].get_IsDefaultShadowEnabledProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def is_default_shadow_enabled(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3].get_IsDefaultShadowEnabled(ctyped.byref(value))
        return value

    @is_default_shadow_enabled.setter
    def is_default_shadow_enabled(self, value: ctyped.type.boolean):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter3].put_IsDefaultShadowEnabled(value)


class MenuFlyout(FlyoutBase):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutStatics,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout,
                   ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout2)

    @property
    def items(self) -> VectorMenuFlyoutItemBase:
        with ctyped.init_com(ctyped.interface.Windows.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemBase], False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout].get_Items(ctyped.byref(obj))
            return VectorMenuFlyoutItemBase(obj)

    @property
    def menu_flyout_presenter_style(self) -> Style:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IStyle, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout].get_MenuFlyoutPresenterStyle(ctyped.byref(obj))
            return Style(obj)

    @menu_flyout_presenter_style.setter
    def menu_flyout_presenter_style(self, value: Style):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout].put_MenuFlyoutPresenterStyle(value[ctyped.interface.Windows.UI.Xaml.IStyle])

    def show_at__(self, target_element: UIElement, point: ctyped.struct.Windows.Foundation.Point) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyout2].ShowAt(target_element[ctyped.interface.Windows.UI.Xaml.IUIElement], point))


class MenuFlyoutItem(MenuFlyoutItemBase):
    _statics = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemFactory,
                ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics,
                ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics2,
                ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics3)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem,
                   ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem2,
                   ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3)

    @classmethod
    @property
    def text_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_TextProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def command_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_CommandProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def command_parameter_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics].get_CommandParameterProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def icon_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics2].get_IconProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @classmethod
    @property
    def keyboard_accelerator_text_override_property(cls) -> DependencyProperty:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IDependencyProperty, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItemStatics3].get_KeyboardAcceleratorTextOverrideProperty(ctyped.byref(obj))
            return DependencyProperty(obj)

    @property
    def text(self) -> ctyped.handle.HSTRING:
        value = ctyped.handle.HSTRING()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem].get_Text(ctyped.byref(value))
        return value

    @text.setter
    def text(self, value: ctyped.handle.HSTRING):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem].put_Text(value)

    @property
    def keyboard_accelerator_text_override(self) -> ctyped.handle.HSTRING:
        value = ctyped.handle.HSTRING()
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3].get_KeyboardAcceleratorTextOverride(ctyped.byref(value))
        return value

    @keyboard_accelerator_text_override.setter
    def keyboard_accelerator_text_override(self, value: ctyped.handle.HSTRING):
        self[ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutItem3].put_KeyboardAcceleratorTextOverride(value)


class Style(DependencyObject):
    _statics = (ctyped.interface.Windows.UI.Xaml.IStyleFactory,)
    _interfaces = (ctyped.interface.Windows.UI.Xaml.IStyle,)

    @classmethod
    def create_instance(cls, target_type: ctyped.struct.Windows.UI.Xaml.Interop.TypeName) -> Style:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IStyle, False) as obj:
            cls[ctyped.interface.Windows.UI.Xaml.IStyleFactory].CreateInstance(target_type, ctyped.byref(obj))
            return Style(obj)

    @property
    def is_sealed(self) -> ctyped.type.boolean:
        value = ctyped.type.boolean()
        self[ctyped.interface.Windows.UI.Xaml.IStyle].get_IsSealed(ctyped.byref(value))
        return value

    @property
    def setters(self) -> SetterBaseCollection:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.ISetterBaseCollection, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.IStyle].get_Setters(ctyped.byref(obj))
            return SetterBaseCollection(obj)

    @property
    def target_type(self) -> ctyped.struct.Windows.UI.Xaml.Interop.TypeName:
        value = ctyped.struct.Windows.UI.Xaml.Interop.TypeName()
        self[ctyped.interface.Windows.UI.Xaml.IStyle].get_TargetType(ctyped.byref(value))
        return value

    @target_type.setter
    def target_type(self, value: ctyped.struct.Windows.UI.Xaml.Interop.TypeName):
        self[ctyped.interface.Windows.UI.Xaml.IStyle].put_TargetType(value)

    @property
    def based_on(self) -> Style:
        with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.IStyle, False) as obj:
            self[ctyped.interface.Windows.UI.Xaml.IStyle].get_BasedOn(ctyped.byref(obj))
            return Style(obj)

    @based_on.setter
    def based_on(self, value: Style):
        self[ctyped.interface.Windows.UI.Xaml.IStyle].put_BasedOn(value[ctyped.interface.Windows.UI.Xaml.IStyle])

    def seal(self) -> bool:
        return ctyped.macro.SUCCEEDED(self[ctyped.interface.Windows.UI.Xaml.IStyle].Seal())


# noinspection PyShadowingBuiltins
@_contextlib.contextmanager  # TODO Array
def box_value(value: _Optional = None, type: _Optional[type[ctyped.CT]] = None) -> _ContextManager[_Optional[ctyped.interface.IInspectable]]:
    if type is None:
        type = _builtins.type(value)
    with ctyped.init_com(ctyped.interface.IInspectable, False) as ref:
        with ctyped.get_winrt(ctyped.interface.Windows.Foundation.IPropertyValueStatics) as prop_statics:
            if value is None:
                prop_statics.CreateEmpty(ctyped.byref(ref))
            else:
                if issubclass(type, ctyped.type.BYTE):
                    func = prop_statics.CreateUInt8
                elif issubclass(type, ctyped.type.INT16):
                    func = prop_statics.CreateInt16
                elif issubclass(type, ctyped.type.INT32):
                    func = prop_statics.CreateInt32
                elif issubclass(type, ctyped.type.UINT32):
                    func = prop_statics.CreateUInt32
                elif issubclass(type, ctyped.type.INT64):
                    func = prop_statics.CreateInt64
                elif issubclass(type, ctyped.type.UINT64):
                    func = prop_statics.CreateUInt64
                elif issubclass(type, ctyped.type.FLOAT):
                    func = prop_statics.CreateSingle
                elif issubclass(type, ctyped.type.DOUBLE):
                    func = prop_statics.CreateDouble
                elif issubclass(type, ctyped.type.WCHAR):
                    func = prop_statics.CreateChar16
                elif issubclass(type, ctyped.type.boolean):
                    func = prop_statics.CreateBoolean
                elif issubclass(type, ctyped.type.HSTRING):
                    func = prop_statics.CreateString
                elif issubclass(type, ctyped.interface.IInspectable):
                    func = prop_statics.CreateInspectable
                elif issubclass(type, ctyped.struct.GUID):
                    func = prop_statics.CreateGuid
                elif issubclass(type, ctyped.struct.Windows.Foundation.DateTime):
                    func = prop_statics.CreateDateTime
                elif issubclass(type, ctyped.struct.Windows.Foundation.TimeSpan):
                    func = prop_statics.CreateTimeSpan
                elif issubclass(type, ctyped.struct.Windows.Foundation.Point):
                    func = prop_statics.CreatePoint
                elif issubclass(type, ctyped.struct.Windows.Foundation.Size):
                    func = prop_statics.CreateSize
                elif issubclass(type, ctyped.struct.Windows.Foundation.Rect):
                    func = prop_statics.CreateRect
                else:
                    yield
                    return
                func(value, ctyped.byref(ref))
        yield ref


# noinspection PyShadowingBuiltins
@_contextlib.contextmanager
def xaml_typename(type: type[ctyped.CT]) -> _ContextManager[ctyped.struct.Windows.UI.Xaml.Interop.TypeName]:  # TODO
    try:
        typename = ctyped.get_winrt_class_name(type)
    except ValueError:
        typename = type.__name__
    name = ctyped.handle.HSTRING.from_string(typename)
    yield ctyped.struct.Windows.UI.Xaml.Interop.TypeName(name, ctyped.enum.Windows.UI.Xaml.Interop.TypeKind.Metadata)


_count = 0


def button_handler(arg: ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler_impl, arg2: ctyped.interface.IInspectable, args: ctyped.interface.Windows.UI.Xaml.IRoutedEventArgs):
    global _count
    _count += 1
    hs = ctyped.handle.HSTRING.from_string(f"Hello World {_count}")
    with ctyped.init_com(ctyped.interface.Windows.UI.Xaml.Controls.IButton, False) as btn:
        args.get_OriginalSource(ctyped.byref(btn))
        button = Button(btn)
        button.content = PropertyValue.create_string(hs)
        FlyoutBase.show_attached_flyout(button)

    return ctyped.const.NOERROR


def button_handler2(arg2: Inspectable, args: RoutedEventArgs) -> int:
    global _count
    _count += 1
    hs = ctyped.handle.HSTRING.from_string(f"Hello World {_count}")
    button = Button(args.original_source)
    button.content = PropertyValue.create_string(hs)
    FlyoutBase.show_attached_flyout(button)
    return ctyped.const.NOERROR


def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == ctyped.const.WM_PAINT:
        if hwnd == _HWND:
            ps = ctyped.struct.PAINTSTRUCT()
            greeting = "Hello World in Win32"
            hdc = ctyped.lib.User32.BeginPaint(hwnd, ctyped.byref(ps))
            ctyped.lib.Gdi32.TextOutW(hdc, 300, 5, greeting, ctyped.lib.msvcrt.wcslen(greeting))
            ctyped.lib.User32.EndPaint(hwnd, ctyped.byref(ps))
    elif msg == ctyped.const.WM_DESTROY:
        ctyped.lib.User32.PostQuitMessage(0)
    else:
        return ctyped.lib.User32.DefWindowProcW(hwnd, msg, wparam, lparam)
    return 0


def main():
    global _HWND
    class_name = "test_winui"
    with open(r'xaml.xml', 'r') as file:
        xaml_data = file.read()

    hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
    wnd_class = ctyped.struct.WNDCLASSW(lpfnWndProc=ctyped.type.WNDPROC(wnd_proc), hInstance=hinstance, lpszClassName=class_name)
    ctyped.lib.User32.RegisterClassW(ctyped.byref(wnd_class))

    hwnd = ctyped.handle.HWND(
        ctyped.lib.User32.CreateWindowExW(0, class_name, "Windows python Win32 Desktop App", ctyped.const.WS_OVERLAPPEDWINDOW | ctyped.const.WS_VISIBLE, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT,
                                          ctyped.const.CW_USEDEFAULT, None, None, hinstance, None))
    # value = ctyped.type.BOOL(True)
    # ctyped.lib.Dwmapi.DwmSetWindowAttribute(hwnd, ctyped.enum.DWMWINDOWATTRIBUTE.USE_IMMERSIVE_DARK_MODE, ctyped.byref(value), ctyped.sizeof(value))
    _HWND = hwnd

    manager = WindowsXamlManager.initialize_for_current_thread()
    print('initialized')
    source = DesktopWindowXamlSource()
    with ctyped.cast_com(source[winrt.UI.Xaml.Hosting.IDesktopWindowXamlSource], ctyped.interface.IDesktopWindowXamlSourceNative) as source_native:
        source_native.AttachToWindow(hwnd)
        hwnd_xaml = ctyped.handle.HWND()
        source_native.get_WindowHandle(ctyped.byref(hwnd_xaml))
        print('got xaml hwnd')
    ctyped.lib.User32.SetWindowPos(hwnd_xaml, 0, 200, 100, 800, 200, ctyped.const.SWP_SHOWWINDOW)
    container = StackPanel()
    container.requested_theme = ctyped.enum.Windows.UI.Xaml.ElementTheme.Dark
    text_block = TextBlock()
    text_block.font_size = 24
    text_block.text = ctyped.handle.HSTRING.from_string('Hello World from Xaml Islands!')
    text_block.HorizontalAlignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    text_block.VerticalAlignment = ctyped.enum.Windows.UI.Xaml.VerticalAlignment.Center
    print('created text block')
    element = DropDownButton(XamlReader.load_with_initial_template_validation(ctyped.handle.HSTRING.from_string(xaml_data)))
    corner_radius = ctyped.struct.Windows.UI.Xaml.CornerRadius(4, 4, 4, 4)
    element.corner_radius = corner_radius
    container.children.append(element)
    print(container.children.get_at(0).opacity)
    button = Button()
    button.corner_radius = corner_radius
    button.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center

    menu = MenuFlyout()
    with xaml_typename(ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter) as tn:
        style = Style.create_instance(tn)
    print(style.target_type)
    setter1 = Setter.create_instance(Control.corner_radius_property, PropertyValue.create_string(ctyped.handle.HSTRING.from_string('4')))
    setter2 = Setter.create_instance(MenuFlyoutPresenter.is_default_shadow_enabled_property, PropertyValue.create_boolean(False))
    style.setters.append(setter1)
    style.setters.append(setter2)
    iterable = style.setters.first()
    while iterable.has_current:
        print(iterable.current)
        iterable.move_next()
    menu.menu_flyout_presenter_style = style
    FlyoutBase.set_attached_flyout(button, menu)

    item1 = MenuFlyoutItem()
    item1.corner_radius = corner_radius
    item1.text = ctyped.handle.HSTRING.from_string('Item 1')
    item2 = MenuFlyoutItem()
    item2.corner_radius = corner_radius
    item2.text = ctyped.handle.HSTRING.from_string('Item 2')
    item3 = MenuFlyoutItem()
    item3.corner_radius = corner_radius
    item3.text = ctyped.handle.HSTRING.from_string('Item 3')
    items = menu.items
    items.append(item1)
    items.append(item2)
    items.append(item3)

    brush = SolidColorBrush.create_instance_with_color(Colors.chocolate)
    button.background = brush
    button.content = text_block
    container.children.append(button)
    token = ctyped.struct.EventRegistrationToken()
    button[winrt.UI.Xaml.Controls.Primitives.IButtonBase].add_Click(ctyped.create_handler_impl(button_handler, ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler_impl), ctyped.byref(token))
    print('added button')
    container.update_layout()
    source.content = container
    print('created xaml')

    hand = RoutedEventHandler.create_instance(button_handler2)[ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler]
    # button[winrt.UI.Xaml.Controls.Primitives.IButtonBase].add_Click(ctyped.cast(hand, ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler_impl).contents)

    hwnd.show()
    hwnd.update()

    msg = ctyped.struct.MSG()
    while ctyped.lib.User32.GetMessageW(ctyped.byref(msg), 0, 0, 0):
        ctyped.lib.User32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.User32.DispatchMessageW(ctyped.byref(msg))


if __name__ == '__main__':
    main()
