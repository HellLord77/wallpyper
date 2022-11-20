import os
import sys

from libs import ctyped

HWND: ctyped.type.HWND = 0
CONTROLLER: ctyped.interface.ICoreWebView2Controller = ctyped.interface.ICoreWebView2Controller()
WEBVIEW: ctyped.interface.ICoreWebView2 = ctyped.interface.ICoreWebView2()
window_class = 'DesktopApp'
title = 'WebView sample'
url = 'https://www.bing.com/'


def _on_create_controller_completed(_, res, ctrl: ctyped.interface.ICoreWebView2Controller) -> ctyped.type.HRESULT:
    print('controller')
    global CONTROLLER, WEBVIEW
    if ctrl:
        CONTROLLER = ctrl
        CONTROLLER.get_CoreWebView2(ctyped.byref(WEBVIEW))

    bounds = ctyped.struct.RECT()
    ctyped.lib.User32.GetClientRect(HWND, ctyped.byref(bounds))
    CONTROLLER.put_Bounds(bounds)

    WEBVIEW.Navigate(url)
    WEBVIEW.AddScriptToExecuteOnDocumentCreated("window.chrome.webview.addEventListener(\'message\', event => alert(event.data));"
                                                "window.chrome.webview.postMessage(window.document.URL);", None)
    return ctyped.const.S_OK


def _on_create_env_completed(_, res, env: ctyped.interface.ICoreWebView2Environment) -> ctyped.type.HRESULT:
    print('environment')
    env.CreateCoreWebView2Controller(HWND, ctyped.create_handler(
        _on_create_controller_completed, ctyped.interface.ICoreWebView2CreateCoreWebView2ControllerCompletedHandler))
    return ctyped.const.S_OK


def webview():
    os.add_dll_directory(r'D:\Projects\wallpyper\helpers')
    ctyped.lib.Ole32.CoInitialize(None)
    ctyped.lib.WebView2Loader.CreateCoreWebView2Environment(
        ctyped.create_handler(_on_create_env_completed, ctyped.interface.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler))


def wnd_proc(hwnd, message, wparam, lparam):
    if message == ctyped.const.WM_SIZE:
        if CONTROLLER:
            bounds = ctyped.struct.RECT()
            ctyped.lib.User32.GetClientRect(hwnd, ctyped.byref(bounds))
            CONTROLLER.put_Bounds(bounds)
    elif message == ctyped.const.WM_DESTROY:
        ctyped.lib.User32.PostQuitMessage(0)
    else:
        return ctyped.lib.User32.DefWindowProcW(hwnd, message, wparam, lparam)
    return 0


def main():
    global HWND
    hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)

    wcex = ctyped.struct.WNDCLASSEXW()
    wcex.style = ctyped.const.CS_HREDRAW | ctyped.const.CS_VREDRAW
    wcex.lpfnWndProc = ctyped.type.WNDPROC(wnd_proc)
    wcex.hInstance = hinstance
    wcex.hCursor = ctyped.handle.HCURSOR.from_idc(ctyped.const.IDC_ARROW)
    wcex.lpszClassName = window_class
    ctyped.lib.User32.RegisterClassExW(ctyped.byref(wcex))

    hwnd = ctyped.lib.User32.CreateWindowExW(0, window_class, title, ctyped.const.WS_OVERLAPPEDWINDOW,
                                             ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, 1200, 900,
                                             ctyped.const.NULL, ctyped.const.NULL, hinstance, ctyped.const.NULL)
    HWND = hwnd
    ctyped.lib.User32.ShowWindow(hwnd, ctyped.const.SW_SHOWNORMAL)
    ctyped.lib.User32.UpdateWindow(hwnd)

    webview()
    # The group or resource is not in the correct state to perform the requested operation

    msg = ctyped.struct.MSG()
    while ctyped.lib.User32.GetMessageW(ctyped.byref(msg), ctyped.const.NULL, 0, 0):
        ctyped.lib.User32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.User32.DispatchMessageW(ctyped.byref(msg))
    sys.exit(msg.wParam)


if __name__ == '__main__':
    main()
