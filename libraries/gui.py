__version__ = '0.0.6'

import atexit
import enum
import functools
import itertools
import os.path
import threading
import time
import typing

import wx
import wx.adv


class Item:
    SEPARATOR = wx.ITEM_SEPARATOR
    NORMAL = wx.ITEM_NORMAL
    CHECK = wx.ITEM_CHECK
    RADIO = wx.ITEM_RADIO
    SUBMENU = wx.ITEM_DROPDOWN


class Icon:
    ERROR = wx.ICON_ERROR
    EXCLAMATION = wx.ICON_EXCLAMATION
    INFORMATION = wx.ICON_INFORMATION
    MASK = wx.ICON_MASK
    NONE = wx.ICON_NONE
    QUESTION = wx.ICON_QUESTION


class Method:
    SET_LABEL = wx.MenuItem.SetItemLabel.__name__


class Property:
    CHECKED = wx.MenuItem.IsChecked.__name__
    ENABLED = wx.MenuItem.IsEnabled.__name__
    UID = wx.MenuItem.GetHelp.__name__


_APP = wx.App()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
_MENU = wx.Menu()
_ICON = wx.Icon()
_ANIMATIONS: list[tuple[itertools.cycle, str]] = []


@functools.cache
def _get_values(cls: type) -> set[str]:
    values = set()
    for name in dir(cls):
        # noinspection PyProtectedMember
        if not (enum._is_descriptor(getattr(cls, name)) or enum._is_dunder(name) or
                enum._is_sunder(name) or enum._is_private(cls.__name__, name)):
            values.add(getattr(cls, name))
    return values


def _get_wrapper(menu_item: wx.MenuItem,
                 callback: typing.Callable,
                 callback_args: tuple,
                 callback_kwargs: dict[str, typing.Any],
                 builtin_args: tuple[str]) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(_: wx.Event):
        builtin_args_ = []
        for builtin_arg in builtin_args:
            if builtin_arg in _get_values(Method):
                builtin_args_.append(getattr(menu_item, builtin_arg))
            elif builtin_arg in _get_values(Property):
                builtin_args_.append(getattr(menu_item, builtin_arg)())
        callback(*builtin_args_, *callback_args, **callback_kwargs)

    return wrapper


def add_menu_item(label: str,
                  kind: typing.Optional[int] = None,
                  check: typing.Optional[bool] = None,
                  enable: typing.Optional[bool] = None,
                  uid: typing.Optional[str] = None,
                  callback: typing.Optional[typing.Callable] = None,
                  callback_args: typing.Optional[tuple] = None,
                  callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                  builtin_args: typing.Optional[tuple[str]] = None,
                  position: typing.Optional[int] = None,
                  menu: wx.Menu = _MENU) -> wx.MenuItem:
    menu_item = menu.Insert(menu.GetMenuItemCount() if position is None else position, wx.ID_ANY,
                            label, uid or '', Item.NORMAL if kind is None else kind)
    if check is not None:
        menu_item.Check(check)
    if enable is not None:
        menu_item.Enable(enable)
    if callback:
        menu.Bind(wx.EVT_MENU, _get_wrapper(menu_item, callback, callback_args or (),
                                            callback_kwargs or {}, builtin_args or ()), menu_item)
    return menu_item


def add_separator() -> wx.MenuItem:
    return add_menu_item('', kind=Item.SEPARATOR)


def add_submenu(label: str,
                kind: typing.Optional[int] = None,
                checks: typing.Optional[tuple[str]] = None,
                enable: typing.Optional[bool] = None,
                items: typing.Optional[dict[str, str]] = None,
                callback: typing.Optional[typing.Callable] = None,
                callback_args: typing.Optional[tuple] = None,
                callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                builtin_args: typing.Optional[tuple[str]] = None,
                position: typing.Optional[int] = None,
                menu: wx.Menu = _MENU) -> wx.MenuItem:
    submenu = wx.Menu()
    for uid, label_ in items.items():
        menu_item = add_menu_item(label_, kind, uid in (checks or ()), label_[0] != '_', uid, callback,
                                  callback_args, callback_kwargs, builtin_args, position, submenu)
        if label_[0] == '_':
            menu_item.SetItemLabel(label_[1:])
    submenu_item = menu.AppendSubMenu(submenu, label)
    if enable is not None:
        submenu_item.Enable(enable)
    return submenu_item


def show_balloon(title: str,
                 text: str,
                 icon: typing.Optional[int] = None) -> bool:
    _TASK_BAR_ICON.SetIcon(_ICON, _APP.GetAppName())
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=Icon.NONE if icon is None else icon)


def _on_right_click(_: wx.Event) -> None:
    _TASK_BAR_ICON.PopupMenu(_MENU)


def _destroy() -> None:
    _ANIMATIONS.clear()
    _MENU.Destroy()
    _TASK_BAR_ICON.RemoveIcon()
    _TASK_BAR_ICON.Destroy()
    _APP.Destroy()


def start_loop(path: str,
               tooltip: typing.Optional[str] = None,
               callback: typing.Optional[typing.Callable] = None,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    _ICON.LoadFile(path)
    _APP.SetAppName(tooltip)
    if callback:
        @functools.wraps(callback)
        def wrapper(_):
            callback(*callback_args or (), **callback_kwargs or {})

        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, wrapper)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(_ICON, tooltip)
    atexit.register(_destroy)
    _APP.MainLoop()


def disable() -> None:
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_LEFT_DCLICK)
    _TASK_BAR_ICON.Unbind(wx.adv.EVT_TASKBAR_CLICK)


def stop_loop() -> None:
    _APP.ExitMainLoop()


@functools.lru_cache(1)
def _get_gif_frames(path: str) -> itertools.cycle:
    animation = wx.adv.Animation(path)
    return itertools.cycle((animation.GetDelay(i), wx.Icon(animation.GetFrame(i).ConvertToBitmap()))
                           for i in range(animation.GetFrameCount()))


def _animate() -> None:
    while _ANIMATIONS:
        delay, icon, tooltip = next(_ANIMATIONS[-1][0]) + (_ANIMATIONS[-1][1],)
        _TASK_BAR_ICON.SetIcon(icon, tooltip)
        time.sleep(delay / 1000)
    else:
        _TASK_BAR_ICON.SetIcon(_ICON, _APP.GetAppName())


def start_animation(path: str,
                    tooltip: typing.Optional[str] = None) -> None:
    _ANIMATIONS.append((_get_gif_frames(path), _APP.GetAppName() if tooltip is None else tooltip))
    if not any(thread.name.startswith(f'{wx.adv.TaskBarIcon.__name__}Animation-') for thread in threading.enumerate()):
        threading.Thread(target=_animate,
                         name=f'{wx.adv.TaskBarIcon.__name__}Animation-{os.path.basename(path)}', daemon=True).start()


def stop_animation(tooltip: typing.Optional[str] = None) -> bool:
    stopped = False
    if _ANIMATIONS:
        if tooltip is None:
            _ANIMATIONS.pop()
            stopped = True
        else:
            for animation in _ANIMATIONS:
                if animation[1] == tooltip:
                    _ANIMATIONS.remove(animation)
                    stopped = True
                    break
    return stopped
