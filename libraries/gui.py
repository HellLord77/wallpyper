import atexit
import typing

import wx
import wx.adv


class ITEM:
    SEPARATOR = wx.ITEM_SEPARATOR
    NORMAL = wx.ITEM_NORMAL
    CHECK = wx.ITEM_CHECK
    RADIO = wx.ITEM_RADIO
    SUBMENU = wx.ITEM_DROPDOWN


class ICON:
    ERROR = wx.ICON_ERROR
    EXCLAMATION = wx.ICON_EXCLAMATION
    INFORMATION = wx.ICON_INFORMATION
    MASK = wx.ICON_MASK
    NONE = wx.ICON_NONE
    QUESTION = wx.ICON_QUESTION


class METHOD:
    SET_LABEL = wx.MenuItem.SetItemLabel.__name__


class PROPERTY:
    IS_CHECKED = wx.Menu.IsChecked.__name__
    IS_ENABLED = wx.Menu.IsEnabled.__name__
    GET_UID = wx.Menu.GetHelpString.__name__


_APP = wx.App()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
_METHOD = set(getattr(METHOD, var) for var in dir(METHOD) if not var.startswith('__'))
_PROPERTY = set(getattr(PROPERTY, var) for var in dir(PROPERTY) if not var.startswith('__'))


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
    item = menu.Insert(menu.GetMenuItemCount() if pos is None else pos,
                       wx.ID_ANY, label, uid or '', kind or wx.ITEM_NORMAL)
    if check is not None:
        item.Check(check)
    if enable is not None:
        item.Enable(enable)
    if callback:
        def wrapped_callback(event: wx.Event) -> None:
            default_args_ = []
            for default_arg in default_args or ():
                if default_arg in _METHOD:
                    default_args_.append(getattr(event.GetEventObject().FindItemById(event.GetId()), default_arg))
                elif default_arg in _PROPERTY:
                    default_args_.append(getattr(event.GetEventObject(), default_arg)(event.GetId()))
            callback(*default_args_, *callback_args or (), **callback_kwargs or {})

        menu.Bind(wx.EVT_MENU, wrapped_callback, item)
    return item


def add_separator() -> wx.MenuItem:
    return add_menu_item('', kind=wx.ITEM_SEPARATOR)


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
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=icon or wx.ICON_NONE)


def start_loop(icon_path: str,
               tooltip: typing.Optional[str] = None,
               callback: typing.Optional[typing.Callable] = None,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    atexit.register(_destroy)
    if callback:
        def wrapped_callback(_: wx.Event) -> None:
            callback(*callback_args or (), **callback_kwargs or {})

        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, wrapped_callback)
    # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(wx.Icon(icon_path, wx.BITMAP_TYPE_ICO), tooltip)
    _APP.MainLoop()


stop_loop = _APP.ExitMainLoop

# TODO: animate icon
