import atexit
import functools
import itertools
import typing

import wx
import wx.adv
import wx.svg


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


class _Arg(type):
    def __new__(mcs, *args, **kwargs):
        instance = super(_Arg, mcs).__new__(mcs, *args, **kwargs)
        instance._values = set(value for var, value in instance.__dict__.items()
                               if not var.startswith('__') and not var.endswith('__'))
        return instance

    def __contains__(cls, item):
        return item in cls._values


class Method(metaclass=_Arg):
    SET_LABEL = wx.MenuItem.SetItemLabel.__name__


class Property(metaclass=_Arg):
    CHECKED = wx.MenuItem.IsChecked.__name__
    ENABLED = wx.MenuItem.IsEnabled.__name__
    UID = wx.MenuItem.GetHelp.__name__


_APP = wx.App()
_ICON = wx.Icon()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()

_TOOLTIP: str = ''
_ANIMATIONS: list[tuple[itertools.cycle, str]] = []


def _get_wrapper(menu_item: wx.MenuItem,
                 callback: typing.Callable,
                 callback_args: tuple,
                 callback_kwargs: dict[str, typing.Any],
                 builtin_args: tuple[str]) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(_: wx.Event):
        builtin_args_ = []
        for builtin_arg in builtin_args:
            if builtin_arg in Method:
                builtin_args_.append(getattr(menu_item, builtin_arg))
            elif builtin_arg in Property:
                builtin_args_.append(getattr(menu_item, builtin_arg)())
        callback(*builtin_args_, *callback_args, **callback_kwargs)

    return wrapper


def _destroy() -> None:
    _MENU.Destroy()
    _TASK_BAR_ICON.RemoveIcon()
    _TASK_BAR_ICON.Destroy()
    _APP.Destroy()


def _on_right_click(_: wx.Event) -> None:
    _TASK_BAR_ICON.PopupMenu(_MENU)


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
    _TASK_BAR_ICON.SetIcon(_ICON, _TOOLTIP)
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=Icon.NONE if icon is None else icon)


def start_loop(path: str,
               tooltip: typing.Optional[str] = None,
               callback: typing.Optional[typing.Callable] = None,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    global _TOOLTIP
    _TOOLTIP = tooltip
    _ICON.LoadFile(path)
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
    for menu_item in _MENU.GetMenuItems():
        menu_item.Enable(False)


def stop_loop() -> None:
    _APP.ExitMainLoop()


@functools.lru_cache(1)
def _get_gif_frames(path: str) -> itertools.cycle:
    animation = wx.adv.Animation(path)
    return itertools.cycle((animation.GetDelay(i), wx.Icon(animation.GetFrame(i).ConvertToBitmap()))
                           for i in range(animation.GetFrameCount()))


def _animate() -> None:
    if _ANIMATIONS:
        delay, icon, tooltip = next(_ANIMATIONS[-1][0]) + (_ANIMATIONS[-1][1],)
        _TASK_BAR_ICON.SetIcon(icon, tooltip)
        wx.CallLater(delay, _animate)
    else:
        _TASK_BAR_ICON.SetIcon(_ICON, _TOOLTIP)


def start_animation(path: str,
                    tooltip: typing.Optional[str] = None) -> None:
    _ANIMATIONS.append((_get_gif_frames(path), _TOOLTIP if tooltip is None else tooltip))
    if len(_ANIMATIONS) == 1:
        wx.CallAfter(_animate)


def stop_animation(tooltip: typing.Optional[str] = None) -> bool:
    stopped = False
    if _ANIMATIONS:
        if tooltip is None:
            _ANIMATIONS.pop()
            stopped = True
        else:
            for animation in _ANIMATIONS:
                if tooltip == animation[1]:
                    _ANIMATIONS.remove(animation)
                    stopped = True
                    break
    return stopped
