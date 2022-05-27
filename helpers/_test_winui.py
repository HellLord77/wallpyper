from __future__ import annotations as _

import builtins as _builtins
import contextlib as _contextlib
import itertools
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
        typename = ctyped.get_winrt_class_name(type)
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
    button.content = winrt.Windows.Foundation.PropertyValue.create_string(f'ToggleButton {{{button.is_checked.value}}}')
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
    corner_radius = ctyped.struct.Windows.UI.Xaml.CornerRadius(4, 4, 4, 4)
    element.corner_radius = corner_radius
    container.children.append(element)
    print(container.children.get_at(0).opacity)
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

    for iid in style.setters.get_iids():
        print(f'{iid}: {ctyped.get_interface_name(iid)}')

    brush = winrt.Windows.UI.Xaml.Media.SolidColorBrush.create_instance_with_color(winrt.Windows.UI.Colors.chocolate)
    button.background = brush
    button.content = text_block
    container.children.append(button)

    button_toggle = winrt.Windows.UI.Xaml.Controls.Primitives.ToggleButton()
    button_toggle.corner_radius = corner_radius
    button_toggle.horizontal_alignment = ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center
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

    container.update_layout()
    source.content = container
    print('created xaml')

    hwnd.show()
    hwnd.update()

    msg = ctyped.struct.MSG()
    while ctyped.lib.User32.GetMessageW(ctyped.byref(msg), 0, 0, 0):
        ctyped.lib.User32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.User32.DispatchMessageW(ctyped.byref(msg))

    source.close()


if __name__ == '__main__':
    main()
