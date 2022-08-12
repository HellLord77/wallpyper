from __future__ import annotations as _

__version__ = '0.0.0'

import atexit
import io
import sys
import threading
import time
import tkinter.messagebox
from typing import Callable, TypeVar
from typing import Optional

import libs.ctyped as ctyped
import win32._gdiplus as gdiplus
import win32._utils as utils
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


def fill_surrounding_rect(hdc, out_x, out_y, out_w, out_h, in_x, in_y, in_w, in_h, argb: ctyped.type.ARGB):
    graphics = gdiplus.Graphics.from_hdc(hdc)
    brush = gdiplus.SolidBrush.from_color(argb)
    if out_x < in_x:
        graphics.fill_rectangle(brush, out_x, out_y, in_x - out_x, out_h)
    if out_y < in_y:
        graphics.fill_rectangle(brush, out_x, out_y, out_w, in_y - out_y)
    if in_x + in_w < out_x + out_w:
        graphics.fill_rectangle(brush, in_x + in_w, out_y, out_x + out_w - (in_x + in_w), out_h)
    if in_y + in_h < out_y + out_h:
        graphics.fill_rectangle(brush, out_x, in_y + in_h, out_w, out_y + out_h - (in_y + in_h))


def _foo(e, s: gui.SystemTray, menu: gui.Menu, item: gui.MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.TRAY)
    menu.show()
    return 0


def _foo2(e: int, s: gui.SystemTray):
    print(s.start_animation(
        r'D:\Projects\Wallpyper\src\res\busy.gif'))  # Gui.get().exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def foo3(e, m: gui.SystemTray, s: gui.SystemTray):
    s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def write(s):
    with open(r'D:\stdout.txt', 'a') as f:
        f.write(s)


def write2(s):
    with open(r'D:\stderr.txt', 'a') as f:
        f.write(s)


def _test_gui():
    p = r'D:\Projects\wallpyper\src\res\tray.png'
    # bind(EVENT_CLOSE, lambda *args: print(6969))
    g = gui.Gui()
    s = gui.SystemTray(p, 'tip')
    menu = gui.Menu()
    not_hidden = menu.append_item('tray icon shown')
    not_hidden.bind(gui.MenuItemEvent.LEFT_UP, lambda *args: print(s.is_shown()))
    it = menu.append_item('stop animate\tright')
    it.bind(gui.MenuItemEvent.LEFT_UP, foo3, (s,))
    it.set_tooltip('important long text tip', 'tip title', p)
    menu.append_item(type=gui.MenuItemType.SEPARATOR)
    ball = menu.append_item('balloon\tright2')
    ball.set_tooltip('another tip')
    ball.bind(gui.MenuItemEvent.RIGHT_UP, lambda *args: print('balloon button right up'))
    ball.bind(gui.MenuItemEvent.LEFT_UP,
              lambda *args: s.show_balloon('very busy', 'mini text', r'D:\Projects\wallpyper\src\res\icon.ico'))
    # print(menu.set_item_image(it, p))
    # ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append_item('text')
    # print(item.get_id(), menu.get_item_id(item))
    menu2 = gui.Menu()
    menu2.append_item('gg', type=gui.MenuItemType.CHECK)
    it_ck = menu.append_item('check', type=gui.MenuItemType.CHECK)
    it_ck.check()
    menu3 = gui.Menu()
    submenu_item = menu.append_item('rad test', submenu=menu3)
    # submenu_item.get_submenu()
    submenu_item.set_icon(r'D:\Projects\wallpyper\src\modules\res\Wallhaven.ico')
    print('set_icon')
    submenu_item.set_submenu(menu3)
    item_icon = menu.append_item('test icon')
    item_icon.bind(gui.MenuItemEvent.LEFT_UP, lambda *args: submenu_item.set_icon(r'D:\Projects\wallpyper\src\modules\Pexels.ico'))
    # menu.set_max_height(100)
    # print(menu.get_max_height())
    for i in range(6):
        menu3.append_item('radio' + str(i), type=gui.MenuItemType.RADIO)
    it7 = menu2.append_item('69')
    it7.bind(gui.MenuItemEvent.HIGHLIGHT, lambda *args: print('hover', args))
    menu2.append_item('new')
    ex = menu.append_item('exit', gui.MenuItemImage.CLOSE)
    ex.bind(gui.MenuItemEvent.LEFT_UP, lambda *args: g.exit_mainloop())
    # print(item.set_image(r'D:\Projects\wallpyper\src\res\tray.png', True))
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

    # s2 = gui.SystemTray(r'D:\Projects\wallpyper\src\res\tray.png', 'tip2')
    # s2.set_animation_speed(5)
    # s2.start_animation(r'D:\Projects\wallpyper\src\res\busy.gif')
    # s2.show()

    def on_exit(*_):
        print('at_exit')

    def on_thread(*_):
        print('thread')
        time.sleep(7)
        print('job_done')

    def end(*_):
        print('end')
        g.exit_mainloop()

    def query_end(*_):
        print('query_end')
        print(hex(g.get_ending_reason()))
        g.exit_mainloop()
        threading.Thread(target=on_thread).start()

    # sys.stdout.write = write
    # sys.stderr.write = write2
    atexit.register(on_exit)
    g.block_end('doing sexy job...')
    g.bind(gui.GuiEvent.QUERY_END, query_end)
    # g.bind(gui.GuiEvent.END, end)
    print(g.get_name())
    g.mainloop()
    print('exit_mainloop')


def _test_settings():
    info = ctyped.struct.SHELLEXECUTEINFOW(lpVerb='open', lpFile='ms-settings:mobile-devices',
                                           nShow=ctyped.const.SW_NORMAL)
    print(ctyped.lib.shell32.ShellExecuteExW(ctyped.byref(info)))


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
        ctyped.lib.kernel32.GetCurrentActCtx(ctyped.byref(handle))
    else:
        ctx = ctyped.struct.ACTCTXW(lpSource=path)
        handle = ctyped.lib.kernel32.CreateActCtxW(ctyped.byref(ctx))
    sz = ctyped.type.SIZE_T()
    if not ctyped.lib.kernel32.QueryActCtxW(
            ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None,
            ctyped.enum.ACTIVATION_CONTEXT_INFO_CLASS.CompatibilityInformationInActivationContext, None, 0,
            ctyped.byref(sz)) and ctyped.lib.kernel32.GetLastError() == ctyped.const.ERROR_INSUFFICIENT_BUFFER:
        buff = ctyped.lib.kernel32.HeapAlloc(ctyped.lib.kernel32.GetProcessHeap(), ctyped.const.HEAP_ZERO_MEMORY, sz)
        if ctyped.lib.kernel32.QueryActCtxW(
                ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None,
                ctyped.enum.ACTIVATION_CONTEXT_INFO_CLASS.CompatibilityInformationInActivationContext,
                buff, sz, ctyped.byref(sz)):
            info = ctyped.cast(buff, ctyped.struct.ACTIVATION_CONTEXT_COMPATIBILITY_INFORMATION).contents
            compatibility = (*ctyped.resize_array(info.Elements, info.ElementCount),)
        if buff:
            ctyped.lib.kernel32.HeapFree(ctyped.lib.kernel32.GetProcessHeap(), 0, buff)
    ctyped.lib.kernel32.ReleaseActCtx(handle)
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


def _dwrite_font():
    bitmap = gdiplus.Bitmap.from_dimension(100, 100)
    with utils.get_d2d1_dc_render_target() as target, ctyped.init_com(
            ctyped.interface.IDWriteFactory, False) as factory, ctyped.init_com(
        ctyped.interface.IDWriteTextFormat, False) as text_format, ctyped.init_com(
        ctyped.interface.ID2D1SolidColorBrush, False) as brush, gdiplus.Graphics.from_image(bitmap).get_managed_hdc() as hdc:
        if target and ctyped.macro.SUCCEEDED(ctyped.lib.DWrite.DWriteCreateFactory(ctyped.enum.DWRITE_FACTORY_TYPE.ISOLATED, ctyped.byref(
                ctyped.get_guid(ctyped.const.IID_IDWriteFactory)), ctyped.byref(factory))):
            factory.CreateTextFormat("Wingdings", None, ctyped.enum.DWRITE_FONT_WEIGHT.NORMAL, ctyped.enum.DWRITE_FONT_STYLE.NORMAL,
                                     ctyped.enum.DWRITE_FONT_STRETCH.NORMAL, 16, "en-US", ctyped.byref(text_format))
            print(text_format.GetFontSize())
            col = ctyped.struct.D3DCOLORVALUE(1, 0, 0, 1)
            print(target.CreateSolidColorBrush(ctyped.byref(col), None, ctyped.byref(brush)))
            rect2 = ctyped.struct.RECT(0, 0, 100, 100)
            rect = ctyped.struct.D2D_RECT_F(0, 0, 100, 100)
            target.BindDC(hdc, ctyped.byref(rect2))
            text = 'Hello World \u0028'
            target.BeginDraw()
            target.DrawText(text, len(text), text_format, ctyped.byref(
                rect), brush, ctyped.enum.D2D1_DRAW_TEXT_OPTIONS.ENABLE_COLOR_FONT, ctyped.enum.DWRITE_MEASURING_MODE.NATURAL)
            target.EndDraw(None, None)
    gdiplus.image_save(bitmap, 'd:\\test.png')


PageAddress = TypeVar('PageAddress', bound=int)
ThreadID = TypeVar('ThreadID', bound=int)
FunctionAddress = TypeVar('FunctionAddress', bound=int)


class Thread(ctyped.type.HANDLE):
    @classmethod
    def create_remote(cls, proc, target: FunctionAddress, arg: Optional[int] = None, suspended: bool = False) -> Thread:
        return cls(ctyped.lib.kernel32.CreateRemoteThread(proc, None, 0, ctyped.type.LPTHREAD_START_ROUTINE(
            target), arg, suspended * ctyped.const.CREATE_SUSPENDED, None))

    def set_priority(self, priority: int) -> bool:
        return bool(ctyped.lib.kernel32.SetThreadPriority(self, priority))

    def set_priority_boost(self, boost: bool = True) -> bool:
        return bool(ctyped.lib.kernel32.SetThreadPriorityBoost(self, not boost))

    def get_priority_boost(self) -> Optional[bool]:
        boost = ctyped.type.BOOL()
        if ctyped.lib.kernel32.GetThreadPriorityBoost(self, ctyped.byref(boost)):
            return not boost.value

    def get_priority(self) -> int:
        return ctyped.lib.kernel32.GetThreadPriority(self)

    def terminate(self, exit_code: int) -> bool:
        return bool(ctyped.lib.kernel32.TerminateThread(self, exit_code))

    def get_exit_code(self) -> Optional[int]:
        exit_code = ctyped.type.DWORD()
        if ctyped.lib.kernel32.GetExitCodeThread(self, ctyped.byref(exit_code)):
            return exit_code.value

    def suspend(self) -> bool:
        return ctyped.lib.kernel32.SuspendThread(self) != -1

    def resume(self) -> bool:
        return ctyped.lib.kernel32.ResumeThread(self) != -1

    def join(self, timeout: int = ctyped.const.INFINITE) -> bool:
        return ctyped.const.WAIT_OBJECT_0 == ctyped.lib.kernel32.WaitForSingleObject(self, timeout)


class RemoteProcess:
    def __init__(self, pid: int, access: int = ctyped.const.PROCESS_ALL_ACCESS):
        self._handle = ctyped.lib.kernel32.OpenProcess(access, False, pid)
        self._libs_remote = {}
        self._libs_local = {}

    def alloc_mem(self, size: int, permission: int = ctyped.const.PAGE_READONLY) -> PageAddress:
        return ctyped.lib.kernel32.VirtualAllocEx(self._handle, None, size, ctyped.const.MEM_COMMIT, permission)

    def free_mem(self, addr: PageAddress) -> bool:
        return bool(ctyped.lib.kernel32.VirtualFreeEx(self._handle, addr, 0, ctyped.const.MEM_RELEASE))

    def read_mem(self, addr: PageAddress, size: int):
        buff = (ctyped.type.c_byte * size)()
        if ctyped.lib.kernel32.ReadProcessMemory(self._handle, addr, ctyped.addressof(buff), size, None):
            return buff

    def write_mem(self, addr: PageAddress, data: bytes | str, size: Optional[int] = None) -> bool:
        if size is None:
            size = (ctyped.sizeof(ctyped.type.c_wchar) if isinstance(data, (
                str)) else ctyped.sizeof(ctyped.type.c_char)) * len(data)
        return bool(ctyped.lib.kernel32.WriteProcessMemory(self._handle, addr, data, size, None))

    def load_lib(self, lib) -> bool:
        lib_path = ctyped.get_lib_path(lib).encode() + b'\0'
        arg_addr = self.alloc_mem(len(lib_path), ctyped.const.PAGE_EXECUTE_READWRITE)
        if arg_addr:
            if self.write_mem(arg_addr, lib_path) and (thread := Thread.create_remote(
                    self._handle, ctyped.addressof_func(ctyped.lib.kernel32.LoadLibraryA), arg_addr)):
                # print(ctyped.cast(self.read_mem(arg_addr, len(lib_path)), ctyped.type.LPSTR).value)
                thread.join()
                if lib_remote := thread.get_exit_code():
                    self._libs_remote[lib] = lib_remote
                    self._libs_local[lib] = ctyped.lib.kernel32.GetModuleHandleA(lib_path)
            self.free_mem(arg_addr)
        return bool(self._libs_remote.get(lib) and self._libs_local.get(lib))

    def unload_lib(self, lib) -> bool:
        if (lib_remote := self._libs_remote.get(lib)) and ctyped.lib.kernel32.FreeLibrary(lib_remote):
            del self._libs_remote[lib]
            return True
        return False

    def get_remote_func(self, func: Callable, lib) -> FunctionAddress:
        lib_local = self._libs_local[lib]
        return self._libs_remote[lib] + ctyped.lib.kernel32.GetProcAddress(
            lib_local, func.__name__.encode()) - lib_local

    def call_func(self, func: FunctionAddress, arg: Optional[int] = None, wait: bool = True) -> Thread:
        thread = Thread.create_remote(self._handle, func, arg)
        if wait:
            thread.join()
        return thread


code = r'''import ctypes
import sys
# import libs.ctyped as ctyped
pid = ctypes.windll.kernel32.GetCurrentProcessId()
ctypes.windll.user32.MessageBoxW(0, f'Hello from Python ({pid=})\n{sys.path}', 'Hello from Python', 0x1000)'''
sys_path = ';'.join(sys.path)


def _test_load_string_from_lib():
    buff = ctyped.char_array(' ' * ctyped.const.MAX_PATH)
    ctyped.lib.user32.LoadStringW(ctyped.lib.kernel32.GetModuleHandleW('shell32.dll'), 5387, buff, ctyped.const.MAX_PATH)
    print(buff.value)


def _test():
    # ctyped.lib.Python.PyRun_SimpleString(code.encode())
    name = 'Progman'

    # hwnd = ctyped.lib.User32.FindWindowW(name, None)
    pid = ctyped.type.DWORD(21112)
    # ctyped.lib.User32.GetWindowThreadProcessId(hwnd, ctyped.byref(pid))
    print(pid)
    proc = RemoteProcess(pid.value)
    print(proc.load_lib(ctyped.lib.python))

    # multi args doesn't work [only first arg is loaded in register]
    # proc.load_lib(ctyped.lib.Kernel32)
    # class Args(ctypes.Structure):
    #     _pack_ = 1
    #     _fields_ = (('dwFreq', ctyped.type.DWORD),
    #                 ('dwDuration', ctyped.type.DWORD))
    # args = Args()
    # args.dwFreq = 750
    # args.dwDuration = 300
    # arg_addr = proc.alloc_mem(ctyped.sizeof(Args), ctyped.const.PAGE_EXECUTE_READWRITE)
    # if arg_addr:
    #     print(ctyped.lib.Kernel32.WriteProcessMemory(proc._handle, arg_addr, ctyped.addressof(args), ctyped.sizeof(args), None))
    #     obj = ctyped.cast(proc.read_mem(arg_addr, ctyped.sizeof(Args)), Args).contents
    #     print(obj.dwFreq, obj.dwDuration)
    #     # proc.write_mem(arg_addr, b_sys_path)
    #     func_addr = proc.get_remote_func(ctyped.lib.Kernel32.Beep, ctyped.lib.Kernel32)
    #     print(proc.call_func(func_addr, arg_addr).get_exit_code())
    #     proc.free_mem(arg_addr)

    print(sys_path)
    arg_addr = proc.alloc_mem(len(sys_path) * 2, ctyped.const.PAGE_EXECUTE_READWRITE)
    if arg_addr:
        proc.write_mem(arg_addr, sys_path)
        func_addr = proc.get_remote_func(ctyped.lib.python.Py_SetPath, ctyped.lib.python)
        proc.call_func(func_addr, arg_addr)
        proc.free_mem(arg_addr)

    func_addr = proc.get_remote_func(ctyped.lib.python.Py_InitializeEx, ctyped.lib.python)
    proc.call_func(func_addr, 0)

    print(code)
    b_code = code.encode() + b'\0'
    arg_addr = proc.alloc_mem(len(b_code), ctyped.const.PAGE_EXECUTE_READWRITE)
    if arg_addr:
        proc.write_mem(arg_addr, b_code)
        func_addr = proc.get_remote_func(ctyped.lib.python.PyRun_SimpleString, ctyped.lib.python)
        print(proc.call_func(func_addr, arg_addr).get_exit_code())
        proc.free_mem(arg_addr)

    func_addr = proc.get_remote_func(ctyped.lib.python.Py_FinalizeEx, ctyped.lib.python)
    print(proc.call_func(func_addr).get_exit_code())
    proc.unload_lib(ctyped.lib.python)


if __name__ == '__main__':
    _test_gui()
    # _test()

    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_NT_HEADERS32, 'OptionalHeader'))
    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_OPTIONAL_HEADER32, 'SizeOfImage'))
    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_OPTIONAL_HEADER32, 'DataDirectory'))
    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_NT_HEADERS64, 'OptionalHeader'))
    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_OPTIONAL_HEADER64, 'SizeOfImage'))
    # print(ctyped.macro.FIELD_OFFSET(ctyped.struct.IMAGE_OPTIONAL_HEADER64, 'DataDirectory'))

    # _test_gui()
    exit()

    ctyped.THREADED_COM = True

    path_ = r'D:\MMDs\洛天依  -  倾杯.mp4'
    path2 = r'D:\test.mp4'
    op = winrt.Windows.Storage.Streams.FileRandomAccessStream.open_async(path_, ctyped.enum.Windows.Storage.FileAccessMode.Read)
    event = threading.Event()


    def handler(*_):
        event.set()
        print(*_)
        return 0


    op.completed = winrt.Windows.Foundation.AsyncOperationCompletedHandlerRandomAccessStream.create_instance(handler)
    event.wait()
    in_stream = op.get_results()
    print(in_stream.size)

    open(path2, 'w').close()
    op_out = winrt.Windows.Storage.Streams.FileRandomAccessStream.open_async(path2, ctyped.enum.Windows.Storage.FileAccessMode.ReadWrite)
    event.clear()
    op_out.completed = winrt.Windows.Foundation.AsyncOperationCompletedHandlerRandomAccessStream.create_instance(handler)
    event.wait()
    out_stream = op_out.get_results()


    def progress(*_):
        print(*_)
        return 0


    op_copy = winrt.Windows.Storage.Streams.RandomAccessStream.copy_async(in_stream, out_stream)
    event.clear()
    op_copy.progress = winrt.Windows.Foundation.AsyncOperationProgressHandlerUINT64UINT64.create_instance(progress)
    op_copy.completed = winrt.Windows.Foundation.AsyncOperationWithProgressCompletedHandlerUINT64UINT64.create_instance(handler)
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
