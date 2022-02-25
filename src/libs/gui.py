__version__ = '0.0.13'

import atexit
import contextlib
import functools
import itertools
import threading
import time
from typing import Any, Callable, Iterable, Mapping, Optional, Union

import wx
import wx.adv


class Item:
    SEPARATOR = wx.ITEM_SEPARATOR
    NORMAL = wx.ITEM_NORMAL
    CHECK = wx.ITEM_CHECK
    RADIO = wx.ITEM_RADIO


class Icon:
    ERROR = wx.ICON_ERROR
    EXCLAMATION = wx.ICON_EXCLAMATION
    INFORMATION = wx.ICON_INFORMATION
    MASK = wx.ICON_MASK
    NONE = wx.ICON_NONE
    QUESTION = wx.ICON_QUESTION


class _Arg(type):
    def __new__(mcs, *args, **kwargs):
        self = super().__new__(mcs, *args, **kwargs)
        self._values = set(getattr(self, var) for var in dir(self) if not var.startswith('_'))
        return self

    def __contains__(cls, item):
        return item in cls._values


class Method(metaclass=_Arg):
    ENABLE = wx.MenuItem.Enable.__name__
    SET_LABEL = wx.MenuItem.SetItemLabel.__name__
    SET_UID = wx.MenuItem.SetMenu.__name__


class Property(metaclass=_Arg):
    CHECKED = wx.MenuItem.IsChecked.__name__
    ENABLED = wx.MenuItem.IsEnabled.__name__
    UID = wx.MenuItem.GetHelp.__name__
    LABEL = wx.MenuItem.GetItemLabelText.__name__


_APP = wx.App()
_FRAME = wx.Frame.__new__(wx.Frame)
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
_MENU = wx.Menu()
_ICON = wx.Icon()
_ANIMATIONS: list[tuple[itertools.cycle, str]] = []
_ANIMATIONS_ = [_ANIMATIONS, []]
_ANIMATION_THREAD = f'{__name__}-{__version__}-{type(_TASK_BAR_ICON).__name__}Animation'


def _get_wrapper(on_click: Callable, menu_args: Iterable[str], args: Iterable,
                 kwargs: Mapping[str, Any], set_state: bool, on_thread: bool, pre_menu_args: bool) -> Callable:
    @functools.wraps(on_click)
    def wrapper(event: Optional[wx.Event] = None):
        menu_item = event.GetEventObject().FindItemById(event.GetId())
        if set_state:
            menu_item.Enable(False)
        args_ = [] if pre_menu_args else list(args)
        for menu_arg in menu_args:
            if menu_arg in Method:
                args_.append(getattr(menu_item, menu_arg))
            elif menu_arg in Property:
                args_.append(getattr(menu_item, menu_arg)())
        if pre_menu_args:
            args_.extend(args)
        try:
            on_click(*args_, **kwargs)
        finally:
            if set_state:
                menu_item.Enable()

    if not on_thread:
        return wrapper

    @functools.wraps(wrapper)
    def wrapper_thread(event: wx.Event) -> threading.Thread:
        thread = threading.Thread(target=wrapper, name=f'{__name__}-{__version__}-{on_click.__name__}', args=(event,))
        thread.start()
        return thread

    return wrapper_thread


def add_menu_item(label: str, kind: int = Item.NORMAL, check: Optional[bool] = None, enable: bool = True,
                  uid: str = '', on_click: Optional[Callable] = None, menu_args: Optional[Iterable[str]] = None,
                  args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None, on_thread: bool = True,
                  change_state: bool = True, position: Optional[int] = None, pre_menu_args: bool = True,
                  menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> wx.MenuItem:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    menu_item: wx.MenuItem = menu.Insert(menu.GetMenuItemCount() if position is None else position, wx.ID_ANY,
                                         label, uid, kind)
    if check is not None:
        menu_item.Check(check)
    menu_item.Enable(enable)
    if on_click is not None:
        menu.Bind(wx.EVT_MENU,
                  _get_wrapper(on_click, () if menu_args is None else menu_args, () if args is None else args,
                               {} if kwargs is None else kwargs, change_state, on_thread, pre_menu_args), menu_item)
    return menu_item


def remove_menu_items(*menus: Union[wx.Menu, wx.MenuItem], menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> int:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    count = 0
    if menus:
        for menu_ in menus:
            if isinstance(menu_, wx.MenuItem):
                menu_ = menu_.GetSubMenu()
            menu.Remove(menu_)
            count += 1
    else:
        for menu_ in menu.GetMenuItems():
            menu.Remove(menu_)
            count += 1
    return count


def add_separator(menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> wx.MenuItem:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    return menu.AppendSeparator()


def add_submenu(label: str, enable: Optional[bool] = None, uid: Optional[str] = None,
                menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> wx.MenuItem:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    menu_item = menu.AppendSubMenu(wx.Menu(), label)
    if enable is not None:
        menu_item.Enable(enable)
    if uid is not None:
        menu_item.SetHelp(uid)
    return menu_item


def get_menu_item_by_uid(uid: str, recursive: bool = True,
                         menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> Optional[wx.MenuItem]:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    menu_: wx.MenuItem
    for menu_ in menu.GetMenuItems():
        if uid == menu_.GetHelp():
            return menu_
        elif recursive and menu_.IsSubMenu():
            if menu_item := get_menu_item_by_uid(uid, recursive, menu_):
                return menu_item


def show_balloon(title: str, text: str, icon: Optional[int] = None) -> bool:
    return _TASK_BAR_ICON.SetIcon(
        _ICON, _APP.GetAppName()) and _TASK_BAR_ICON.ShowBalloon(title, text, flags=Icon.NONE if icon is None else icon)


def _on_right_click(_: wx.Event):
    _TASK_BAR_ICON.PopupMenu(_MENU)


def _destroy():
    _ANIMATIONS.clear()
    _MENU.Destroy()
    _TASK_BAR_ICON.RemoveIcon()
    _TASK_BAR_ICON.Destroy()
    _FRAME.Destroy()
    _APP.Destroy()


def start_loop(path: str, tooltip: Optional[str] = None, callback: Optional[Callable] = None,
               args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
    _APP.SetAppName(tooltip)
    _ICON.LoadFile(path)
    if callback:
        @functools.wraps(callback)
        def wrapper(_: wx.Event):
            callback(*() if args is None else args, **{} if kwargs is None else kwargs)

        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, wrapper)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(_ICON, tooltip)
    _FRAME.__init__(None)
    _FRAME.Bind(wx.EVT_CLOSE, stop_loop)
    _APP.Bind(wx.EVT_END_SESSION, stop_loop)
    atexit.register(_destroy)
    _APP.MainLoop()


def stop_loop(_: Optional[wx.CloseEvent] = None):
    _APP.ExitMainLoop()


def disable_events():
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_LEFT_DCLICK)
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_CLICK)


@functools.lru_cache(1)
def _get_gif_frames(path: str) -> itertools.cycle:
    animation = wx.adv.Animation(path)
    return itertools.cycle((animation.GetDelay(index), wx.Icon(animation.GetFrame(index).ConvertToBitmap()))
                           for index in range(animation.GetFrameCount()))


def _animation_worker() -> bool:
    while True:
        try:
            delay, icon = next(_ANIMATIONS_[0][-1][0])
            _TASK_BAR_ICON.SetIcon(icon, _ANIMATIONS_[0][-1][1])
        except IndexError:
            return _TASK_BAR_ICON.IsIconInstalled() and _TASK_BAR_ICON.SetIcon(_ICON, _APP.GetAppName())
        else:
            time.sleep(delay / 1000)


def _start_animation() -> bool:
    if _ANIMATIONS and _ANIMATIONS_[0] is _ANIMATIONS:
        if not any(thread.name == _ANIMATION_THREAD for thread in threading.enumerate()):
            threading.Thread(target=_animation_worker, name=_ANIMATION_THREAD, daemon=True).start()
            return True
    return False


def start_animation(path: str, tooltip: Optional[str] = None) -> bool:
    _ANIMATIONS.append((_get_gif_frames(path), _APP.GetAppName() if tooltip is None else tooltip))
    return _start_animation()


def stop_animation(tooltip: Optional[str] = None) -> bool:
    stopped = False
    if tooltip is None:
        with contextlib.suppress(IndexError):
            _ANIMATIONS.pop()
        stopped = True
    else:
        for animation in _ANIMATIONS:
            if animation[1] == tooltip:
                _ANIMATIONS.remove(animation)
                stopped = True
                break
    return stopped


def disable_animation(disable: bool = True) -> bool:
    if _ANIMATIONS_[not disable] is _ANIMATIONS:
        _ANIMATIONS_.reverse()
    if not disable:
        _start_animation()
    return _ANIMATIONS_[1] is _ANIMATIONS
