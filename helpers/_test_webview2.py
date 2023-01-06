import os
import sys
import threading

from libs import ctyped
from libs.ctyped.interface.package import WebView2
from libs.ctyped.lib import user32, kernel32, WebView2Loader
from win32.browser import _webview2

window_class = 'DesktopApp'
title = 'WebView sample'
url = 'https://www.bing.com/'


class CLS:
    HWND: ctyped.type.HWND = 0
    CONTROLLER: _webview2.CoreWebView2Controller = None
    WEBVIEW: _webview2.CoreWebView2 = None
    # response: Optional[_webview2.CoreWebView2WebResourceResponse] = None


def handle(sender: WebView2.ICoreWebView2,
           args: WebView2.ICoreWebView2WebResourceRequestedEventArgs) -> ctyped.type.HRESULT:
    arg = _webview2.CoreWebView2WebResourceRequestedEventArgs(args)
    if CLS.response:
        arg.response = CLS.response
    return ctyped.const.NOERROR


def _create_controller_completed(result: ctyped.type.HRESULT, controller: WebView2.ICoreWebView2Controller) -> ctyped.type.HRESULT:
    print('controller')
    if ctyped.macro.SUCCEEDED(result):
        CLS.CONTROLLER = _webview2.CoreWebView2Controller(controller)
        # CLS.CONTROLLER.add_ref()
        CLS.WEBVIEW = CLS.CONTROLLER.core_web_view_2

    bounds = ctyped.struct.RECT()
    user32.GetClientRect(CLS.HWND, ctyped.byref(bounds))
    CLS.CONTROLLER.bounds = bounds

    # print(CLS.WEBVIEW.AddWebResourceRequestedFilter('*', ctyped.enum.COREWEBVIEW2_WEB_RESOURCE_CONTEXT.IMAGE))
    # token = ctyped.struct.EventRegistrationToken()
    # with ctyped.interface.create_handler(handle, WebView2.ICoreWebView2WebResourceRequestedEventHandler) as handler:
    #     CLS.WEBVIEW.add_WebResourceRequested(handler, ctyped.byref(token))
    CLS.WEBVIEW.navigate(url)
    # WEBVIEW.AddScriptToExecuteOnDocumentCreated('window.addEventListener("DOMContentLoaded", (event) => { alert("HellLord"); });', None)
    return ctyped.const.S_OK


def _create_environment_completed(result: ctyped.type.HRESULT, environment: WebView2.ICoreWebView2Environment) -> ctyped.type.HRESULT:
    print('environment')
    if ctyped.macro.SUCCEEDED(result):
        with ctyped.interface.create_handler(_create_controller_completed, WebView2.ICoreWebView2CreateCoreWebView2ControllerCompletedHandler) as handler:
            environment.CreateCoreWebView2Controller(CLS.HWND, handler)
        envv = _webview2.CoreWebView2Environment(environment)
        print(envv.browser_version_string)
        # CLS.response = envv.create_web_resource_response(None, 418, "I'm a teapot", '')
        return ctyped.const.NOERROR
    else:
        return result


def webview():
    os.add_dll_directory(r'D:\Projects\wallpyper\helpers')
    data_path = r'D:\Projects\wallpyper\helpers\WebView2'
    with ctyped.interface.create_handler(
            _create_environment_completed, WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler) as handler:
        if ctyped.macro.SUCCEEDED(WebView2Loader.CreateCoreWebView2EnvironmentWithOptions(
                ctyped.NULLPTR, data_path, ctyped.NULLPTR, handler)):
            print('wait')


def wnd_proc(hwnd, message, wparam, lparam):
    if message == ctyped.const.WM_SIZE:
        if CLS.CONTROLLER:
            bounds = ctyped.struct.RECT()
            user32.GetClientRect(hwnd, ctyped.byref(bounds))
            CLS.CONTROLLER.bounds = bounds
    elif message == ctyped.const.WM_DESTROY:
        user32.PostQuitMessage(0)
    else:
        return user32.DefWindowProcW(hwnd, message, wparam, lparam)
    return 0


def main():
    global CLS
    hinstance = kernel32.GetModuleHandleW(None)

    wcex = ctyped.struct.WNDCLASSEXW()
    wcex.style = ctyped.const.CS_HREDRAW | ctyped.const.CS_VREDRAW
    wcex.lpfnWndProc = ctyped.type.WNDPROC(wnd_proc)
    wcex.hInstance = hinstance
    wcex.hCursor = ctyped.handle.HCURSOR.from_idc(ctyped.const.IDC_ARROW)
    wcex.lpszClassName = window_class
    user32.RegisterClassExW(ctyped.byref(wcex))

    hwnd = user32.CreateWindowExW(0, window_class, title, ctyped.const.WS_OVERLAPPEDWINDOW,
                                  ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, 1200, 900,
                                  ctyped.const.NULL, ctyped.const.NULL, hinstance, ctyped.const.NULL)
    CLS.HWND = hwnd
    user32.ShowWindow(hwnd, ctyped.const.SW_SHOWNORMAL)

    webview()

    msg = ctyped.struct.MSG()
    while user32.GetMessageW(ctyped.byref(msg), ctyped.const.NULL, 0, 0):
        user32.TranslateMessage(ctyped.byref(msg))
        user32.DispatchMessageW(ctyped.byref(msg))

    del CLS
    sys.exit(msg.wParam)


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
    # main()
