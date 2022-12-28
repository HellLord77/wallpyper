import os
import sys
from typing import Optional

from libs import ctyped
from libs.ctyped.interface.package import WebView2
from win32 import _webview2

HWND: ctyped.type.HWND = 0
CONTROLLER: WebView2.ICoreWebView2Controller = WebView2.ICoreWebView2Controller()
WEBVIEW: WebView2.ICoreWebView2 = WebView2.ICoreWebView2()
window_class = 'DesktopApp'
title = 'WebView sample'
url = 'https://www.bing.com/'
response: Optional[_webview2.CoreWebView2WebResourceResponse] = None


def handle(sender: WebView2.ICoreWebView2,
           args: WebView2.ICoreWebView2WebResourceRequestedEventArgs) -> ctyped.type.HRESULT:
    arg = _webview2.CoreWebView2WebResourceRequestedEventArgs(args)
    if response:
        arg.response = response
    return ctyped.const.NOERROR


def _on_create_controller_completed(res, ctrl: WebView2.ICoreWebView2Controller) -> ctyped.type.HRESULT:
    print('controller')
    global CONTROLLER
    if ctrl:
        CONTROLLER = ctrl
        CONTROLLER.AddRef()
        CONTROLLER.get_CoreWebView2(ctyped.byref(WEBVIEW))

    bounds = ctyped.struct.RECT()
    ctyped.lib.user32.GetClientRect(HWND, ctyped.byref(bounds))
    CONTROLLER.put_Bounds(bounds)

    print(WEBVIEW.AddWebResourceRequestedFilter('*', ctyped.enum.COREWEBVIEW2_WEB_RESOURCE_CONTEXT.IMAGE))
    token = ctyped.struct.EventRegistrationToken()
    handler = ctyped.create_handler(handle, WebView2.ICoreWebView2WebResourceRequestedEventHandler)
    WEBVIEW.add_WebResourceRequested(handler, ctyped.byref(token))
    WEBVIEW.Navigate(url)
    # WEBVIEW.AddScriptToExecuteOnDocumentCreated('window.addEventListener("DOMContentLoaded", (event) => { alert("HellLord"); });', None)
    return ctyped.const.S_OK


def _on_create_env_completed(res, env: WebView2.ICoreWebView2Environment) -> ctyped.type.HRESULT:
    print('environment')
    env.CreateCoreWebView2Controller(HWND, ctyped.create_handler(
        _on_create_controller_completed, WebView2.ICoreWebView2CreateCoreWebView2ControllerCompletedHandler))
    envv = _webview2.CoreWebView2Environment(env)
    print(envv.browser_version_string)
    global response
    response = envv.create_web_resource_response(None, 418, "I'm a teapot", '')
    return ctyped.const.S_OK


def webview():
    os.add_dll_directory(r'D:\Projects\wallpyper\helpers')
    ctyped.lib.ole32.CoInitialize(None)
    ctyped.lib.WebView2Loader.CreateCoreWebView2Environment(ctyped.create_handler(
        _on_create_env_completed, WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler))


def wnd_proc(hwnd, message, wparam, lparam):
    global CONTROLLER
    if message == ctyped.const.WM_SIZE:
        if CONTROLLER:
            bounds = ctyped.struct.RECT()
            ctyped.lib.user32.GetClientRect(hwnd, ctyped.byref(bounds))
            CONTROLLER.put_Bounds(bounds)
    elif message == ctyped.const.WM_DESTROY:
        ctyped.lib.user32.PostQuitMessage(0)
    else:
        return ctyped.lib.user32.DefWindowProcW(hwnd, message, wparam, lparam)
    return 0


def main():
    global HWND
    hinstance = ctyped.lib.kernel32.GetModuleHandleW(None)

    wcex = ctyped.struct.WNDCLASSEXW()
    wcex.style = ctyped.const.CS_HREDRAW | ctyped.const.CS_VREDRAW
    wcex.lpfnWndProc = ctyped.type.WNDPROC(wnd_proc)
    wcex.hInstance = hinstance
    wcex.hCursor = ctyped.handle.HCURSOR.from_idc(ctyped.const.IDC_ARROW)
    wcex.lpszClassName = window_class
    ctyped.lib.user32.RegisterClassExW(ctyped.byref(wcex))

    hwnd = ctyped.lib.user32.CreateWindowExW(0, window_class, title, ctyped.const.WS_OVERLAPPEDWINDOW,
                                             ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, 1200, 900,
                                             ctyped.const.NULL, ctyped.const.NULL, hinstance, ctyped.const.NULL)
    HWND = hwnd
    ctyped.lib.user32.ShowWindow(hwnd, ctyped.const.SW_SHOWNORMAL)
    ctyped.lib.user32.UpdateWindow(hwnd)

    webview()
    # The group or resource is not in the correct state to perform the requested operation

    msg = ctyped.struct.MSG()
    while ctyped.lib.user32.GetMessageW(ctyped.byref(msg), ctyped.const.NULL, 0, 0):
        ctyped.lib.user32.TranslateMessage(ctyped.byref(msg))
        ctyped.lib.user32.DispatchMessageW(ctyped.byref(msg))

    print(CONTROLLER.Release())
    sys.exit(msg.wParam)


if __name__ == '__main__':
    main()
