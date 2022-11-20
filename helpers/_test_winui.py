from __future__ import annotations as _

import builtins as _builtins
import contextlib as _contextlib
import itertools
import sys
from typing import Optional as _Optional, ContextManager as _ContextManager

from libs import ctyped
from libs.ctyped import winrt

_HWND: int = None


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
        typename = ctyped._get_winrt_class_name(type)
    except ValueError:
        typename = type.__name__
    name = ctyped.handle.HSTRING.from_string(typename)
    yield ctyped.struct.Windows.UI.Xaml.Interop.TypeName(name, ctyped.enum.Windows.UI.Xaml.Interop.TypeKind.Metadata)


def button_handler(arg2, args: winrt.Windows.UI.Xaml.RoutedEventArgs) -> int:
    button = winrt.Windows.UI.Xaml.Controls.Button(args.original_source)
    text = winrt.Windows.UI.Xaml.Controls.TextBlock(button.content)
    text.font_size = text.font_size * 0.9
    text.text = f"Button {{{text.font_size}}}"
    # FlyoutBase.show_attached_flyout(button)
    return ctyped.const.NOERROR


count = 0


def repeat_button_handler(arg2, args: winrt.Windows.UI.Xaml.RoutedEventArgs) -> int:
    global count
    count += 1
    button = winrt.Windows.UI.Xaml.Controls.Primitives.RepeatButton(args.original_source)
    button.content = winrt.Windows.Foundation.PropertyValue.create_string(f'RepeatButton {{{count}}}')
    return ctyped.const.NOERROR


def toggle_button_handler(arg2, args: winrt.Windows.UI.Xaml.RoutedEventArgs) -> int:
    button = winrt.Windows.UI.Xaml.Controls.Primitives.ToggleButton(args.original_source)
    button.content = winrt.Windows.Foundation.PropertyValue.create_string(f'ToggleButton {{{button.is_checked}}}')
    return ctyped.const.NOERROR


def app_bar_button_handler(arg2, args: winrt.Windows.UI.Xaml.RoutedEventArgs) -> int:
    button = winrt.Windows.UI.Xaml.Controls.AppBarButton(args.original_source)
    icon = winrt.Windows.UI.Xaml.Controls.SymbolIcon(button.icon).symbol
    symbols = itertools.cycle(ctyped.enum.Windows.UI.Xaml.Controls.Symbol)
    while icon != next(symbols):
        pass
    symbol = next(symbols)
    button.icon = winrt.Windows.UI.Xaml.Controls.SymbolIcon.create_instance_with_symbol(symbol)
    button.label = str(symbol)
    return ctyped.const.NOERROR


def adjust_layout(hwnd: ctyped.type.HWND):
    rect = ctyped.struct.RECT()
    ctyped.lib.User32.GetClientRect(hwnd, ctyped.byref(rect))
    ctyped.lib.User32.SetWindowPos(_HWND, None, 0, 0, rect.right, rect.bottom, ctyped.const.SWP_SHOWWINDOW)


def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == ctyped.const.WM_DESTROY:
        ctyped.lib.User32.PostQuitMessage(0)
    elif msg == ctyped.const.WM_SIZE:
        adjust_layout(hwnd)
    else:
        return ctyped.lib.User32.DefWindowProcW(hwnd, msg, wparam, lparam)
    return 0


SPRING_ANIM: winrt.Windows.UI.Composition.SpringVector3NaturalMotionAnimation = None


def pointer_enter(sender, arg):
    ele = winrt.Windows.UI.Xaml.FrameworkElement(sender)
    ele.center_point = ctyped.struct.Windows.Foundation.Numerics.Vector3(ele.actual_width / 2, ele.actual_height / 2, 1)
    SPRING_ANIM.final_value = ctyped.struct.Windows.Foundation.Numerics.Vector3(1.25, 1.25, 1.25)
    ele.start_animation(SPRING_ANIM)
    return ctyped.const.NOERROR


def pointer_exit(sender, arg):
    SPRING_ANIM.final_value = ctyped.struct.Windows.Foundation.Numerics.Vector3(1.0, 1.0, 1.0)
    winrt.Windows.UI.Xaml.UIElement(sender).start_animation(SPRING_ANIM)
    return ctyped.const.NOERROR


def find_child(parent: winrt.Windows.UI.Xaml.DependencyObject, name: str = '') -> _Optional[winrt.Windows.UI.Xaml.DependencyObject]:
    for index in range(winrt.Windows.UI.Xaml.Media.VisualTreeHelper.get_children_count(parent)):
        child = winrt.Windows.UI.Xaml.Media.VisualTreeHelper.get_child(parent, index)
        if name == winrt.Windows.UI.Xaml.FrameworkElement(child).name:
            return child
        else:
            child = find_child(child, name)
            if child is not None:
                return child


def main():
    global _HWND
    class_name = "test_winui"
    with open(r'xaml.xml') as file:
        xaml_data = file.read()
    corner_radius = ctyped.struct.Windows.UI.Xaml.CornerRadius(4, 4, 4, 4)

    hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
    wnd_class = ctyped.struct.WNDCLASSW(lpfnWndProc=ctyped.type.WNDPROC(wnd_proc), hInstance=hinstance, lpszClassName=class_name)
    ctyped.lib.User32.RegisterClassW(ctyped.byref(wnd_class))

    hwnd = ctyped.handle.HWND(ctyped.lib.User32.CreateWindowExW(
        0, class_name, "Windows python Win32 Desktop App", ctyped.const.WS_OVERLAPPEDWINDOW | ctyped.const.WS_VISIBLE, ctyped.const.CW_USEDEFAULT,
        ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, None, None, hinstance, None))
    # value = ctyped.type.BOOL(True)
    # ctyped.lib.Dwmapi.DwmSetWindowAttribute(hwnd, ctyped.enum.DWMWINDOWATTRIBUTE.USE_IMMERSIVE_DARK_MODE, ctyped.byref(value), ctyped.sizeof(value))

    source = winrt.Windows.UI.Xaml.Hosting.DesktopWindowXamlSource()
    with ctyped.cast_com(source[ctyped.interface.Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource], ctyped.interface.IDesktopWindowXamlSourceNative) as source_native:
        source_native.AttachToWindow(hwnd)
        hwnd_xaml = ctyped.handle.HWND()
        source_native.get_WindowHandle(ctyped.byref(hwnd_xaml))
        _HWND = hwnd_xaml.value
        print('got xaml hwnd')
    adjust_layout(hwnd)

    container = winrt.Windows.UI.Xaml.Controls.StackPanel()
    container.requested_theme = ctyped.enum.Windows.UI.Xaml.ElementTheme.Dark
    text_block = winrt.Windows.UI.Xaml.Controls.TextBlock()
    text_block.font_size = 24
    text_block.text = 'TextBlock'
    text_block.HorizontalAlignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    text_block.VerticalAlignment = ctyped.enum.Windows.UI.Xaml.VerticalAlignment.Center
    print('created text block')

    element = winrt.Windows.UI.Xaml.Controls.DropDownButton(winrt.Windows.UI.Xaml.Markup.XamlReader.load_with_initial_template_validation(xaml_data))
    element.corner_radius = corner_radius
    container.children.append(element)

    print(element.find_name('FlyoutItem'))
    fly = winrt.Windows.UI.Xaml.Controls.Primitives.FlyoutBase.get_attached_flyout(element)
    print(fly, bool(fly))

    button = winrt.Windows.UI.Xaml.Controls.Button()
    button.corner_radius = corner_radius
    button.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center

    button.click += winrt.Windows.UI.Xaml.RoutedEventHandler.create_instance(button_handler)

    menu = winrt.Windows.UI.Xaml.Controls.MenuFlyout()
    with xaml_typename(ctyped.interface.Windows.UI.Xaml.Controls.IMenuFlyoutPresenter) as tn:
        style = winrt.Windows.UI.Xaml.Style.create_instance(tn)
    print(style.target_type)
    setter1 = winrt.Windows.UI.Xaml.Setter.create_instance(winrt.Windows.UI.Xaml.Controls.Control.corner_radius_property, winrt.Windows.Foundation.PropertyValue.create_string('4'))
    setter2 = winrt.Windows.UI.Xaml.Setter.create_instance(winrt.Windows.UI.Xaml.Controls.MenuFlyoutPresenter.is_default_shadow_enabled_property, winrt.Windows.Foundation.PropertyValue.create_boolean(False))
    style.setters.append(setter1)
    style.setters.append(setter2)
    iterable = style.setters.first()
    while iterable.has_current:
        print(iterable.current)
        iterable.move_next()
    print(style.is_sealed)
    menu.menu_flyout_presenter_style = style
    winrt.Windows.UI.Xaml.Controls.Primitives.FlyoutBase.set_attached_flyout(button, menu)

    item1 = winrt.Windows.UI.Xaml.Controls.MenuFlyoutItem()
    item1.corner_radius = corner_radius
    item1.text = 'Item 1'
    item2 = winrt.Windows.UI.Xaml.Controls.MenuFlyoutItem()
    item2.corner_radius = corner_radius
    item2.text = 'Item 2'
    item3 = winrt.Windows.UI.Xaml.Controls.MenuFlyoutItem()
    item3.corner_radius = corner_radius
    item3.text = 'Item 3'
    items = menu.items
    items.append(item1)
    items.append(item2)
    items.append(item3)
    print(items.size)

    # for iid in style.setters.get_iids(): TODO IVector
    #     print(f'{iid}: {ctyped.get_interface_name(iid)}')

    # brush = winrt.Windows.UI.Xaml.Media.SolidColorBrush.create_instance_with_color(winrt.Windows.UI.Colors.chocolate)
    # button.background = brush
    button.content = text_block
    container.children.append(button)

    class OverrideTest(ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonOverrides_impl):
        inner_interface = None

        def GetIids(self, iidCount: ctyped.Pointer[ctyped.type.ULONG],
                    iids: ctyped.Pointer[ctyped.Pointer[ctyped.struct.IID]]) -> ctyped.type.HRESULT:
            print('GetIids')
            return self.inner_interface.GetIids(iidCount, iids)

        def QueryInterface(self, riid: ctyped.Pointer[ctyped.struct.IID], ppvObject: ctyped.type.LPVOID) -> ctyped.type.HRESULT:
            val = ctyped.type.LPOLESTR()
            ctyped.lib.Ole32.StringFromIID(riid, ctyped.byref(val))
            print(val.value, ctyped.get_interface_name(val.value))
            if val.value == '{D20E4C28-F18B-491A-9A45-F1A04A9369A4}':
                return super().QueryInterface(riid, ppvObject)
            else:
                return self.inner_interface.QueryInterface(riid, ppvObject)

        def OnToggle(self):
            print('OnToggle')
            with ctyped.cast_com(self.inner_interface, ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonOverrides) as overrides:
                return overrides.OnToggle()

    with ctyped.get_winrt(ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IToggleButtonFactory) as button_factory:
        base_interface = OverrideTest()
        inner_interface = ctyped.interface.IInspectable()
        value = ctyped.interface.Windows.UI.Xaml.Controls.Primitives.IToggleButton()
        button_factory.CreateInstance(ctyped.cast(base_interface, ctyped.interface.IInspectable),
                                      ctyped.byref(inner_interface), ctyped.byref(value))
    base_interface.inner_interface = inner_interface
    button_toggle = winrt.Windows.UI.Xaml.Controls.Primitives.ToggleButton(value)
    button_toggle.corner_radius = corner_radius
    button_toggle.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    button_toggle.content = winrt.Windows.Foundation.PropertyValue.create_string('OverrideToggleButton')
    container.children.append(button_toggle)

    button_toggle = winrt.Windows.UI.Xaml.Controls.Primitives.ToggleButton()
    button_toggle.corner_radius = corner_radius
    button_toggle.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    button_toggle.is_checked = True
    button_toggle.content = winrt.Windows.Foundation.PropertyValue.create_string('ToggleButton')
    button_toggle.click += winrt.Windows.UI.Xaml.RoutedEventHandler.create_instance(toggle_button_handler)
    container.children.append(button_toggle)

    button_repeat = winrt.Windows.UI.Xaml.Controls.Primitives.RepeatButton()
    button_repeat.corner_radius = corner_radius
    button_repeat.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    button_repeat.content = winrt.Windows.Foundation.PropertyValue.create_string('RepeatButton')
    button_repeat.click += winrt.Windows.UI.Xaml.RoutedEventHandler.create_instance(repeat_button_handler)
    container.children.append(button_repeat)

    button_link = winrt.Windows.UI.Xaml.Controls.HyperlinkButton()
    button_link.corner_radius = corner_radius
    button_link.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    button_link.content = winrt.Windows.Foundation.PropertyValue.create_string('HyperlinkButton')
    button_link.navigate_uri = winrt.Windows.Foundation.Uri.create_uri('ms-settings:windowsupdate')
    tip = winrt.Windows.UI.Xaml.Controls.ToolTip()
    tip.content = winrt.Windows.Foundation.PropertyValue.create_string('Windows Update')
    winrt.Windows.UI.Xaml.Controls.ToolTipService.set_tool_tip(button_link, tip)
    container.children.append(button_link)

    app_bar_button = winrt.Windows.UI.Xaml.Controls.AppBarButton()
    app_bar_button.corner_radius = corner_radius
    app_bar_button.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
    app_bar_button.min_width = 150
    app_bar_button.icon = winrt.Windows.UI.Xaml.Controls.SymbolIcon.create_instance_with_symbol(ctyped.enum.Windows.UI.Xaml.Controls.Symbol.Previous)
    app_bar_button.label = str(ctyped.enum.Windows.UI.Xaml.Controls.Symbol.Previous)
    app_bar_button.click += winrt.Windows.UI.Xaml.RoutedEventHandler.create_instance(app_bar_button_handler)
    container.children.append(app_bar_button)

    brush = winrt.Windows.UI.Xaml.Media.LinearGradientBrush()
    stop1 = winrt.Windows.UI.Xaml.Media.GradientStop()
    stop1.color = winrt.Windows.UI.Colors.yellow
    stop1.offset = 0
    brush.gradient_stops.append(stop1)
    stop2 = winrt.Windows.UI.Xaml.Media.GradientStop()
    stop2.color = winrt.Windows.UI.Colors.red
    stop2.offset = 0.25
    brush.gradient_stops.append(stop2)
    stop3 = winrt.Windows.UI.Xaml.Media.GradientStop()
    stop3.color = winrt.Windows.UI.Colors.blue
    stop3.offset = 0.5
    brush.gradient_stops.append(stop3)
    stop4 = winrt.Windows.UI.Xaml.Media.GradientStop()
    stop4.color = winrt.Windows.UI.Colors.lime_green
    stop4.offset = 0.75
    brush.gradient_stops.append(stop4)
    button.background = brush

    global SPRING_ANIM
    wnd: winrt.Windows.UI.Xaml.Window = winrt.Windows.UI.Xaml.Window.current
    SPRING_ANIM = wnd.compositor.create_spring_vector3_animation()
    SPRING_ANIM.target = 'Scale'
    button.pointer_entered += winrt.Windows.UI.Xaml.Input.PointerEventHandler.create_instance(pointer_enter)
    button.pointer_exited += winrt.Windows.UI.Xaml.Input.PointerEventHandler.create_instance(pointer_exit)

    container.update_layout()
    source.content = container

    hwnd.show()
    hwnd.update()

    msg = ctyped.struct.MSG()
    while ctyped.lib.User32.GetMessageW(ctyped.byref(msg), 0, 0, 0):
        ctyped.lib.User32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.User32.DispatchMessageW(ctyped.byref(msg))

    source.close()


def foo(p: winrt.Windows.UI.Xaml.ApplicationInitializationCallbackParams):
    print(p)
    return ctyped.const.NOERROR


def application():
    ctyped.lib.ComBase.RoInitialize(ctyped.enum.RO_INIT_TYPE.SINGLETHREADED)
    app = winrt.Windows.UI.Xaml.Application()
    # dh = winrt.Windows.UI.Core.DispatchedHandler.create_instance(disp)
    # patcher = winrt.Windows.UI.Core.CoreDispatcher()
    # res = winrt.Windows.Foundation.Uri.create_uri('file://D:/Projects/wallpyper/helpers/app.xml')
    # winrt.Windows.UI.Xaml.Application.load_component(app, res)
    bar = winrt.Windows.UI.Xaml.ApplicationInitializationCallback.create_instance(foo)
    winrt.Windows.UI.Xaml.Application.start(bar)
    window = winrt.Windows.UI.Xaml.Window.current
    print(bool(window), window)
    app.exit()
    sys.exit(69)


if __name__ == '__main__':
    main()
