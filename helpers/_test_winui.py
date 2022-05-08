from libs import ctyped

winrt = ctyped.interface.Windows

HWND = None


def button_handler(*args):
    print(args)
    return ctyped.const.NOERROR


def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == ctyped.const.WM_PAINT:
        if hwnd == HWND:
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
    global HWND
    class_name = "test_winui"
    with open(r'..\helpers\xaml.xml', 'r') as file:
        xaml_data = file.read()

    hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
    wnd_class = ctyped.struct.WNDCLASSW(lpfnWndProc=ctyped.type.WNDPROC(wnd_proc), hInstance=hinstance, lpszClassName=class_name)
    ctyped.lib.User32.RegisterClassW(ctyped.byref(wnd_class))

    hwnd = ctyped.handle.HWND(
        ctyped.lib.User32.CreateWindowExW(0, class_name, "Windows python Win32 Desktop App", ctyped.const.WS_OVERLAPPEDWINDOW | ctyped.const.WS_VISIBLE, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT,
                                          ctyped.const.CW_USEDEFAULT, None, None, hinstance, None))
    # value = ctyped.type.BOOL(True)
    # ctyped.lib.Dwmapi.DwmSetWindowAttribute(hwnd, ctyped.enum.DWMWINDOWATTRIBUTE.USE_IMMERSIVE_DARK_MODE, ctyped.byref(value), ctyped.sizeof(value))
    HWND = hwnd

    with ctyped.get_winrt(winrt.UI.Xaml.Hosting.IWindowsXamlManagerStatics) as manager_statics, ctyped.init_com(winrt.UI.Xaml.Hosting.IWindowsXamlManager, False) as manager:
        manager_statics.InitializeForCurrentThread(ctyped.byref(manager))
        print('initialized')
        with ctyped.get_winrt(winrt.UI.Xaml.Hosting.IDesktopWindowXamlSource, True) as source:
            with ctyped.cast_com(source, ctyped.interface.IDesktopWindowXamlSourceNative) as source_native:
                source_native.AttachToWindow(hwnd)
                hwnd_xaml = ctyped.handle.HWND()
                source_native.get_WindowHandle(ctyped.byref(hwnd_xaml))
                print('got xaml hwnd')
        ctyped.lib.User32.SetWindowPos(hwnd_xaml, 0, 200, 100, 800, 200, ctyped.const.SWP_SHOWWINDOW)
        with ctyped.get_winrt(winrt.UI.Xaml.Controls.IStackPanel, True) as xaml_container:
            with ctyped.cast_com(xaml_container, ctyped.interface.Windows.UI.Xaml.IFrameworkElement2) as xaml_element:
                xaml_element.put_RequestedTheme(ctyped.enum.Windows.UI.Xaml.ElementTheme.Dark)
            with ctyped.cast_com(xaml_container, winrt.UI.Xaml.Controls.IPanel) as panel:
                with ctyped.get_winrt(winrt.UI.Xaml.Controls.ITextBlock, True) as text_block:
                    text_block.put_Text(ctyped.handle.HSTRING.from_string('Hello World from Xaml Islands!'))
                    with ctyped.cast_com(text_block, winrt.UI.Xaml.IFrameworkElement) as text_element:
                        text_element.put_VerticalAlignment(ctyped.enum.Windows.UI.Xaml.VerticalAlignment.Center)
                        text_element.put_HorizontalAlignment(ctyped.enum.Windows.UI.Xaml.HorizontalAlignment.Center)
                    text_block.put_FontSize(24)
                    print('created text block')
                    with ctyped.get_winrt(winrt.UI.Xaml.Markup.IXamlReaderStatics) as reader_statics:
                        with ctyped.init_com(winrt.UI.Xaml.IUIElement, False) as xaml_element:
                            reader_statics.Load(ctyped.handle.HSTRING.from_string(xaml_data), ctyped.byref(xaml_element))
                            print('loaded xaml')
                            with ctyped.init_com(winrt.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.IUIElement], False) as children:
                                panel.get_Children(ctyped.byref(children))
                                children.Append(xaml_element)

                    with ctyped.get_winrt(winrt.UI.Xaml.Controls.IButton, True) as button:
                        with ctyped.cast_com(button, winrt.UI.Xaml.Controls.IControl) as button_control:
                            with ctyped.get_winrt(winrt.UI.IColorsStatics) as colors_statics:
                                color = ctyped.struct.Windows.UI.Color()
                                colors_statics.get_Lime(ctyped.byref(color))
                                with ctyped.init_com(winrt.UI.Xaml.Media.ISolidColorBrush, False) as solid_brush:
                                    with ctyped.get_winrt(winrt.UI.Xaml.Media.ISolidColorBrushFactory) as brush_factory:
                                        brush_factory.CreateInstanceWithColor(color, ctyped.byref(solid_brush))
                                    with ctyped.cast_com(solid_brush, winrt.UI.Xaml.Media.IBrush) as brush:
                                        button_control.put_Background(brush)
                        with ctyped.cast_com(button, winrt.UI.Xaml.Controls.IContentControl) as button_content:
                            button_content.put_Content(text_block)
                        with ctyped.init_com(winrt.Foundation.Collections.IVector[ctyped.interface.Windows.UI.Xaml.IUIElement], False) as children:
                            panel.get_Children(ctyped.byref(children))
                            with ctyped.cast_com(button, winrt.UI.Xaml.IUIElement) as button_element:
                                children.Append(button_element)
                        with ctyped.cast_com(button, winrt.UI.Xaml.Controls.Primitives.IButtonBase) as button_base:
                            token = ctyped.struct.EventRegistrationToken()
                            button_base.add_Click(ctyped.create_handler_impl(button_handler, ctyped.interface.Windows.UI.Xaml.IRoutedEventHandler_impl), ctyped.byref(token))
                    print('added button')
            with ctyped.cast_com(xaml_container, winrt.UI.Xaml.IUIElement) as container_element:
                container_element.UpdateLayout()
                source.put_Content(container_element)
    print('created xaml')

    hwnd.show()
    hwnd.update()

    msg = ctyped.struct.MSG()
    while ctyped.lib.User32.GetMessageW(ctyped.byref(msg), 0, 0, 0):
        ctyped.lib.User32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.User32.DispatchMessageW(ctyped.byref(msg))


if __name__ == '__main__':
    main()
