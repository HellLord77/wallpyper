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
    IS_CHECKED = wx.Menu.IsChecked.__name__
    IS_ENABLED = wx.Menu.IsEnabled.__name__
    GET_UID = wx.Menu.GetHelpString.__name__


_APP = wx.App()
_ICON = wx.Icon()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()


class _Animate:
    animated = False
    default_tooltip = ''

    @staticmethod
    def animate(_: itertools.cycle,
                __: str) -> None:
        pass

    default_animate = animate


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
                  default_args: typing.Optional[tuple[str]] = None,
                  pos: typing.Optional[int] = None,
                  menu: wx.Menu = _MENU) -> wx.MenuItem:
    item = menu.Insert(menu.GetMenuItemCount() if pos is None else pos, wx.ID_ANY,
                       label, uid or '', Item.NORMAL if kind is None else kind)
    if check is not None:
        item.Check(check)
    if enable is not None:
        item.Enable(enable)
    if callback:
        @functools.wraps(callback)
        def wrapper(event: wx.Event) -> None:
            default_args_ = []
            for default_arg in default_args or ():
                if default_arg in Method:
                    default_args_.append(getattr(event.GetEventObject().FindItemById(event.GetId()), default_arg))
                elif default_arg in Property:
                    default_args_.append(getattr(event.GetEventObject(), default_arg)(event.GetId()))
            callback(*default_args_, *callback_args or (), **callback_kwargs or {})

        menu.Bind(wx.EVT_MENU, wrapper, item)
    return item


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
                default_args: typing.Optional[tuple[str]] = None,
                pos: typing.Optional[int] = None,
                menu: wx.Menu = _MENU) -> wx.MenuItem:
    submenu = wx.Menu()
    checks = checks or ()
    for uid, label_ in items.items():
        item = add_menu_item(label_, kind, uid in checks, label_[0] != '_', uid, callback,
                             callback_args, callback_kwargs, default_args, pos, submenu)
        if label_[0] == '_':
            item.SetItemLabel(label_[1:])
    submenu_item = menu.AppendSubMenu(submenu, label)
    if enable is not None:
        submenu_item.Enable(enable)
    return submenu_item


def show_balloon(title: str,
                 text: str,
                 icon: typing.Optional[int] = None) -> bool:
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=Icon.NONE if icon is None else icon)


def start_loop(path: str,
               tooltip: typing.Optional[str] = None,
               callback: typing.Optional[typing.Callable] = None,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    _ICON.LoadFile(path)
    _Animate.default_tooltip = tooltip
    if callback:
        @functools.wraps(callback)
        def wrapper(_: wx.Event) -> None:
            callback(*callback_args or (), **callback_kwargs or {})

        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, wrapper)
    # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(_ICON, tooltip)
    atexit.register(_destroy)
    _APP.MainLoop()


def stop_loop() -> None:
    stop_animation()
    _APP.ExitMainLoop()


@functools.lru_cache(1)
def _extract_gif(path: str) -> itertools.cycle:
    animation = wx.adv.Animation(path)
    return itertools.cycle((animation.GetDelay(i), wx.Icon(animation.GetFrame(i).ConvertToBitmap()))
                           for i in range(animation.GetFrameCount()))


def start_animation(path: str,
                    tooltip: typing.Optional[str] = None) -> bool:
    if _Animate.animated:
        return False
    else:
        _Animate.animated = True

        def animate(frames: itertools.cycle,
                    tooltip_: str) -> None:
            delay, icon = next(frames)
            _TASK_BAR_ICON.SetIcon(icon, tooltip_)
            wx.CallLater(delay, _Animate.animate, frames, tooltip_)

        _Animate.animate = animate
        wx.CallAfter(animate, _extract_gif(path), _Animate.default_tooltip if tooltip is None else tooltip)
        return True


def stop_animation() -> bool:
    if _Animate.animated:
        _Animate.animated = False
        _Animate.animate.__code__ = _Animate.default_animate.__code__
        _TASK_BAR_ICON.SetIcon(_ICON, _Animate.default_tooltip)
        return True
    else:
        return False
