__version__ = '0.0.9'

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
        instance = super().__new__(mcs, *args, **kwargs)
        instance._values = set(getattr(instance, var) for var in dir(instance) if not var.startswith('_'))
        return instance

    def __contains__(cls, item):
        return item in cls._values


class Method(metaclass=_Arg):
    ENABLE = wx.MenuItem.Enable.__name__
    SET_LABEL = wx.MenuItem.SetItemLabel.__name__


class Property(metaclass=_Arg):
    CHECKED = wx.MenuItem.IsChecked.__name__
    ENABLED = wx.MenuItem.IsEnabled.__name__
    HELP = wx.MenuItem.GetHelp.__name__
    LABEL = wx.MenuItem.GetItemLabelText.__name__


_APP = wx.App()
_FRAME = wx.Frame.__new__(wx.Frame)
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
_MENU = wx.Menu()
_ICON = wx.Icon()
_ANIMATIONS: list[tuple[itertools.cycle, str]] = []
_ANIMATIONS_ = [_ANIMATIONS, []]
_ANIMATION_THREAD = f'{type(_TASK_BAR_ICON).__name__}Animation'


def _get_wrapper(menu_item: wx.MenuItem, on_click: Callable, args: Iterable,
                 kwargs: Mapping[str, Any], extra_args: Iterable[str]) -> Callable:
    @functools.wraps(on_click)
    def wrapper(_: wx.Event):
        extra_args_ = []
        for extra_arg in extra_args:
            if extra_arg in Method:
                extra_args_.append(getattr(menu_item, extra_arg))
            elif extra_arg in Property:
                extra_args_.append(getattr(menu_item, extra_arg)())
        on_click(*extra_args_, *args, **kwargs)

    return wrapper


def add_menu_item(label: str, kind: Optional[int] = None, check: Optional[bool] = None, enable: Optional[bool] = None,
                  help_text: Optional[str] = None, on_click: Optional[Callable] = None, args: Optional[Iterable] = None,
                  kwargs: Optional[Mapping[str, Any]] = None, extra_args: Optional[Iterable[str]] = None,
                  position: Optional[int] = None, menu: Union[wx.Menu, wx.MenuItem] = _MENU) -> wx.MenuItem:
    if isinstance(menu, wx.MenuItem):
        menu = menu.GetSubMenu()
    menu_item: wx.MenuItem = menu.Insert(menu.GetMenuItemCount() if position is None else position,
                                         wx.ID_ANY, label, help_text or '', Item.NORMAL if kind is None else kind)
    if check is not None:
        menu_item.Check(check)
    if enable is not None:
        menu_item.Enable(enable)
    if on_click:
        menu.Bind(wx.EVT_MENU, _get_wrapper(menu_item, on_click, args or (), kwargs or {}, extra_args or ()), menu_item)
    return menu_item


def add_separator(menu: wx.Menu = _MENU) -> wx.MenuItem:
    return menu.AppendSeparator()


def add_submenu(label: str, enable: Optional[bool] = None, menu: wx.Menu = _MENU) -> wx.MenuItem:
    menu_item = menu.AppendSubMenu(wx.Menu(), label)
    if enable is not None:
        menu_item.Enable(enable)
    return menu_item


def show_balloon(title: str, text: str, icon: Optional[int] = None) -> bool:
    return _TASK_BAR_ICON.SetIcon(
        _ICON, _APP.GetAppName()) and _TASK_BAR_ICON.ShowBalloon(title, text, flags=Icon.NONE if icon is None else icon)


def _on_right_click(_: wx.Event) -> None:
    _TASK_BAR_ICON.PopupMenu(_MENU)


def _destroy() -> None:
    _ANIMATIONS.clear()
    _MENU.Destroy()
    _TASK_BAR_ICON.RemoveIcon()
    _TASK_BAR_ICON.Destroy()
    _FRAME.Destroy()
    _APP.Destroy()


def start_loop(path: str, tooltip: Optional[str] = None, callback: Optional[Callable] = None,
               args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> None:
    _ICON.LoadFile(path)
    _APP.SetAppName(tooltip)
    if callback:
        @functools.wraps(callback)
        def wrapper(_: wx.Event):
            callback(*args or (), **kwargs or {})

        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, wrapper)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(_ICON, tooltip)
    _FRAME.__init__(None)
    _FRAME.Bind(wx.EVT_CLOSE, stop_loop)
    _APP.Bind(wx.EVT_END_SESSION, stop_loop)
    atexit.register(_destroy)
    _APP.MainLoop()


def stop_loop(_: Optional[wx.CloseEvent] = None) -> None:
    _APP.ExitMainLoop()


def disable_events() -> None:
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_LEFT_DCLICK)
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_CLICK)


@functools.lru_cache(1)
def _get_gif_frames(path: str) -> itertools.cycle:
    animation = wx.adv.Animation(path)
    return itertools.cycle((animation.GetDelay(i),
                            wx.Icon(animation.GetFrame(i).ConvertToBitmap())) for i in range(animation.GetFrameCount()))


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
