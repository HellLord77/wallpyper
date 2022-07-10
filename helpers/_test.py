__version__ = '0.0.0'

import io
import sys
import threading
import time
import tkinter.messagebox
from typing import Callable
from typing import Optional

import libs.ctyped as ctyped
import win32._gdiplus as _gdiplus
import win32.gui as gui
from libs.ctyped import winrt


def exception_handler(excepthook: Callable, *args, **kwargs):
    stderr = sys.stderr
    sys.stderr = io.StringIO()
    excepthook(*args, **kwargs)
    sys.stderr.seek(0)
    root = tkinter.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    while not isinstance(args, type):
        args = args[0]
    tkinter.messagebox.showerror(args.__name__, sys.stderr.read())
    root.destroy()
    sys.stderr = stderr


# sys.excepthook = types.MethodType(exception_handler, sys.excepthook)
# threading.excepthook = types.MethodType(exception_handler, threading.excepthook)


def _fill_empty_rect(hdc, out_x, out_y, out_w, out_h, in_x, in_y, in_w, in_h, argb: ctyped.type.ARGB):
    graphics = _gdiplus.Graphics.from_hdc(hdc)
    brush = _gdiplus.SolidFill.from_color(argb)
    if out_x < in_x:
        graphics.fill_rect(brush, out_x, out_y, in_x - out_x, out_h)
    if out_y < in_y:
        graphics.fill_rect(brush, out_x, out_y, out_w, in_y - out_y)
    if in_x + in_w < out_x + out_w:
        graphics.fill_rect(brush, in_x + in_w, out_y, out_x + out_w - (in_x + in_w), out_h)
    if in_y + in_h < out_y + out_h:
        graphics.fill_rect(brush, out_x, in_y + in_h, out_w, out_y + out_h - (in_y + in_h))


def _foo(e, s: gui.SystemTray, menu: gui.Menu, item: gui._MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.TRAY)
    menu.show()
    return 0


def _foo2(e: int, s: gui.SystemTray):
    print(s.start_animation(
        r'D:\Projects\Wallpyper\src\resources\busy.gif'))  # Gui.get().exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def foo3(e, m: gui.SystemTray, s: gui.SystemTray):
    s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def _test_gui():
    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    # bind(EVENT_CLOSE, lambda *args: print(6969))
    g = gui.Gui()
    s = gui.SystemTray(p, 'tip')
    menu = gui.Menu()
    not_hidden = menu.append_item('tray icon shown')
    not_hidden.bind(gui.MenuItemEvent.LEFT_UP, lambda *args: print(s.is_shown()))
    it = menu.append_item('stop animate\tright')
    print(it.is_enabled())
    it.bind(gui.MenuItemEvent.LEFT_UP, foo3, (s,))
    it.set_tooltip('important long text tip', 'tip title', p)
    menu.append_item(type=gui.MenuItemType.SEPARATOR)
    ball = menu.append_item('balloon\tright2')
    ball.set_tooltip('another tip')
    ball.bind(gui.MenuItemEvent.RIGHT_UP, lambda *args: print('balloon button right up'))
    ball.bind(gui.MenuItemEvent.LEFT_UP,
              lambda *args: s.show_balloon('very busy', 'mini text', r'D:\Projects\wallpyper\src\resources\icon.ico'))
    # print(menu.set_item_image(it, p))
    # ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append_item('text')
    # print(item.get_id(), menu.get_item_id(item))
    menu2 = gui.Menu()
    menu2.append_item('gg', type=gui.MenuItemType.CHECK)
    it_ck = menu.append_item('check', type=gui.MenuItemType.CHECK)
    it_ck.check()
    # it_ck.set_image(p)  # TODO do not die after click
    menu3 = gui.Menu()
    menu.append_item('rad test', submenu=menu3)
    # menu.set_max_height(100)
    # print(menu.get_max_height())
    for i in range(6):
        menu3.append_item('radio' + str(i), type=gui.MenuItemType.RADIO)
    it7 = menu2.append_item('69')
    it7.bind(gui.MenuItemEvent.HIGHLIGHT, lambda *args: print('hover', args))
    menu2.append_item('new')
    ex = menu.append_item('exit', gui.MenuItemImage.CLOSE)
    ex.bind(gui.MenuItemEvent.LEFT_UP, lambda *args: g.exit_mainloop())
    # print(item.set_image(r'D:\Projects\wallpyper\src\resources\tray.png', True))
    # menu.set_item_submenu(item, menu2)
    item.set_submenu(menu2)
    item.set_image(p)
    item.set_tooltip('https://www.google.com')
    g.bind(gui.GuiEvent.DISPLAY_CHANGE, lambda *args: print('display', args))

    s.bind(gui.SystemTrayEvent.RIGHT_UP, _foo, (menu, item))
    s.bind(gui.SystemTrayEvent.LEFT_DOUBLE, _foo2)
    s.bind(gui.SystemTrayEvent.BALLOON_SHOW, lambda *args: print('show_balloon'))
    s.bind(gui.SystemTrayEvent.BALLOON_HIDE, lambda *args: print('show_balloon hide'))
    s.bind(gui.SystemTrayEvent.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()

    # s2 = SysTray(r'D:\Projects\wallpyper\src\resources\tray.png', 'tip2')
    # s2.set_animation_speed(5)
    # s2.start_animation(r'D:\Projects\wallpyper\src\resources\busy.gif')
    # s2.show()

    g.mainloop()
    g.destroy()
    print('exit')


def _test_settings():
    info = ctyped.struct.SHELLEXECUTEINFOW(lpVerb='open', lpFile='ms-settings:mobile-devices',
                                           nShow=ctyped.const.SW_NORMAL)
    print(ctyped.lib.Shell32.ShellExecuteExW(ctyped.byref(info)))


class ToastDismiss(ctyped.interface.Windows.Foundation.ITypedEventHandler_impl[
                       ctyped.interface.Windows.UI.Notifications.IToastNotification,
                       ctyped.interface.Windows.UI.Notifications.IToastDismissedEventArgs]):
    # noinspection PyPep8Naming
    def Invoke(self, sender: ctyped.interface.Windows.UI.Notifications.IToastNotification,
               args: ctyped.interface.Windows.UI.Notifications.IToastDismissedEventArgs) -> ctyped.type.HRESULT:
        print('invoke', self, sender, args)
        reason = ctyped.enum.Windows.UI.Notifications.ToastDismissalReason()
        args.get_Reason(ctyped.byref(reason))
        print(reason)
        return ctyped.const.NOERROR


def hand_dismissed(sender: winrt.Windows.UI.Notifications.ToastNotification, args: winrt.Windows.UI.Notifications.ToastDismissedEventArgs):
    print(args.reason)
    return ctyped.const.NOERROR


def activ(sender: winrt.Windows.UI.Notifications.ToastNotification, a):
    print(winrt.Windows.UI.Notifications.ToastActivatedEventArgs(a).argument, a)
    return 0


def _test_toast():
    ctyped.THREADED_COM = True
    aumi = 'HellLord.Wallpyper'
    xml_data = '''
<toast launch="action=viewDownload&amp;downloadId=9438108">
  
  <visual>
    <binding template="ToastGeneric">
      <text>Downloading this week's new music...</text>
      <progress
        title="{progressTitle}"
        value="{progressValue}"
        valueStringOverride="{progressValueString}"
        status="{progressStatus}"/>
    </binding>
  </visual>

  <actions>

    <action
      activationType="background"
      arguments="action=pauseDownload&amp;downloadId=9438108"
      content="Pause"/>

    <action
      activationType="background"
      arguments="action=cancelDownload&amp;downloadId=9438108"
      content="Cancel"/>
    
  </actions>
  
</toast>'''

    notifier = winrt.Windows.UI.Notifications.ToastNotificationManager.create_toast_notifier_with_id(aumi)
    xml = winrt.Windows.Data.Xml.Dom.XmlDocument()
    xml.load_xml(xml_data)
    toast = winrt.Windows.UI.Notifications.ToastNotification.create_toast_notification(xml)
    toast.activated += winrt.Windows.Foundation.TypedEventHandlerToastNotificationInspectable.create_instance(activ)
    toast.dismissed += winrt.Windows.Foundation.TypedEventHandlerToastNotificationToastDismissedEventArgs.create_instance(hand_dismissed)
    notifier.show(toast)
    print('wait')
    _wait()


def _get_context_compatibility(path: Optional[str] = None) -> tuple[ctyped.struct.COMPATIBILITY_CONTEXT_ELEMENT, ...]:
    compatibility = ()
    if path is None:
        handle = ctyped.type.HANDLE()
        ctyped.lib.Kernel32.GetCurrentActCtx(ctyped.byref(handle))
    else:
        ctx = ctyped.struct.ACTCTXW(lpSource=path)
        handle = ctyped.lib.Kernel32.CreateActCtxW(ctyped.byref(ctx))
    sz = ctyped.type.SIZE_T()
    if not ctyped.lib.Kernel32.QueryActCtxW(
            ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None,
            ctyped.enum.ACTIVATION_CONTEXT_INFO_CLASS.CompatibilityInformationInActivationContext, None, 0,
            ctyped.byref(sz)) and ctyped.lib.Kernel32.GetLastError() == ctyped.const.ERROR_INSUFFICIENT_BUFFER:
        buff = ctyped.lib.Kernel32.HeapAlloc(ctyped.lib.Kernel32.GetProcessHeap(), ctyped.const.HEAP_ZERO_MEMORY, sz)
        if ctyped.lib.Kernel32.QueryActCtxW(
                ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None,
                ctyped.enum.ACTIVATION_CONTEXT_INFO_CLASS.CompatibilityInformationInActivationContext,
                buff, sz, ctyped.byref(sz)):
            info = ctyped.cast(buff, ctyped.struct.ACTIVATION_CONTEXT_COMPATIBILITY_INFORMATION).contents
            compatibility = (*ctyped.resize_array(info.Elements, info.ElementCount),)
        if buff:
            ctyped.lib.Kernel32.HeapFree(ctyped.lib.Kernel32.GetProcessHeap(), 0, buff)
    ctyped.lib.Kernel32.ReleaseActCtx(handle)
    return compatibility


def set_lock():
    path_lock = r'C:\Users\ratul\AppData\Local\Temp\Wallpyper\wallhaven-z87rqj.jpg'
    op_lock = winrt.Windows.Storage.Streams.FileRandomAccessStream.open_async(path_lock, ctyped.enum.Windows.Storage.FileAccessMode.Read)
    event2 = threading.Event()

    def handle_lock(*_):
        event2.set()
        print(*_)
        return 0

    op_lock.completed = winrt.Windows.Foundation.AsyncOperationCompletedHandlerRandomAccessStream.create_instance(handle_lock)
    event2.wait()
    in_stream_lock = op_lock.get_results()
    ac = winrt.Windows.System.UserProfile.LockScreen.set_image_stream_async(in_stream_lock)
    event2.clear()
    ac.completed = winrt.Windows.Foundation.AsyncActionCompletedHandler.create_instance(handle_lock)
    event2.wait()
    print(ac.get_results())


def _test():
    from libs import locales
    for lang in locales.Language:
        print(locales.Language.get(lang))


if __name__ == '__main__':
    _test()
    exit()

    ctyped.THREADED_COM = True

    path = r'D:\MMDs\洛天依  -  倾杯.mp4'
    path2 = r'D:\test.mp4'
    op = winrt.Windows.Storage.Streams.FileRandomAccessStream.open_async(path, ctyped.enum.Windows.Storage.FileAccessMode.Read)
    event = threading.Event()


    def handle(*_):
        event.set()
        print(*_)
        return 0


    op.completed = winrt.Windows.Foundation.AsyncOperationCompletedHandlerRandomAccessStream.create_instance(handle)
    event.wait()
    in_stream = op.get_results()
    print(in_stream.size)

    open(path2, 'w').close()
    op_out = winrt.Windows.Storage.Streams.FileRandomAccessStream.open_async(path2, ctyped.enum.Windows.Storage.FileAccessMode.ReadWrite)
    event.clear()
    op_out.completed = winrt.Windows.Foundation.AsyncOperationCompletedHandlerRandomAccessStream.create_instance(handle)
    event.wait()
    out_stream = op_out.get_results()


    def progress(*_):
        print(*_)
        return 0


    op_copy = winrt.Windows.Storage.Streams.RandomAccessStream.copy_async(in_stream, out_stream)
    event.clear()
    op_copy.progress = winrt.Windows.Foundation.AsyncOperationProgressHandlerUINT64UINT64.create_instance(progress)
    op_copy.completed = winrt.Windows.Foundation.AsyncOperationWithProgressCompletedHandlerUINT64UINT64.create_instance(handle)
    event.wait()

    in_stream.close()
    out_stream.close()

    # print(ctyped.get_winrt_class_name(ctyped.interface.Windows.Foundation.Collections.IMap[ctyped.type.HSTRING, ctyped.type.HSTRING]))
    # map_hs = winrt.Windows.Foundation.Collections.MapHSTRINGHSTRING()
    # print(map_hs.size)
    # print(ctyped.get_winrt_class_name(ctyped.interface.Windows.Foundation.IAsyncActionProgressHandler_impl))
    # print(win32.wallpaper.save_lock(r'd:\lock.jpg'))
    # _test_toast()
    # _test_gui()
    # _test_settings()
    # _wait()
    sys.exit()
