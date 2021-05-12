import atexit
import typing

import wx
import wx.adv
import wx.lib.embeddedimage


class ITEM:
    SEPARATOR = -1
    NORMAL = 0
    CHECK = 1
    RADIO = 2
    SUBMENU = 3


class ICON:
    ERROR = 512
    EXCLAMATION = 256
    INFORMATION = 2048
    MASK = 790272
    NONE = 262144
    QUESTION = 1024


class METHOD:
    SET_LABEL = 'SetItemLabel'


class PROPERTY:
    IS_CHECKED = 'IsChecked'
    IS_ENABLED = 'IsEnabled'
    GET_UID = 'GetHelpString'


_APP = wx.App()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
_CALLBACKS = set()
_METHOD = set(getattr(METHOD, var) for var in dir(METHOD) if not var.startswith('__') and not var.endswith('__'))
_PROPERTY = set(getattr(PROPERTY, var) for var in dir(PROPERTY) if not var.startswith('__') and not var.endswith('__'))


def _destroy() -> None:
    _MENU.Destroy()
    _TASK_BAR_ICON.RemoveIcon()
    _TASK_BAR_ICON.Destroy()
    _APP.Destroy()


def _on_right_click(_: wx.Event) -> None:
    _TASK_BAR_ICON.PopupMenu(_MENU)
    for callback in _CALLBACKS:
        callback()


def add_menu_item(label: str,
                  kind: typing.Optional[int] = None,
                  check: typing.Optional[bool] = None,
                  enable: typing.Optional[bool] = None,
                  uid: typing.Optional[str] = None,
                  callback: typing.Optional[typing.Callable] = None,
                  callback_args: typing.Optional[tuple] = None,
                  callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                  args: typing.Optional[tuple[str]] = None,
                  menu: wx.Menu = _MENU) -> wx.MenuItem:
    item = menu.Append(wx.ID_ANY, label, uid or '', kind or ITEM.NORMAL)
    if check is not None:
        item.Check(check)
    if enable is not None:
        item.Enable(enable)
    if callback:
        def wrapped_callback(event):
            extra_args = []
            for arg in args or ():
                if arg in _METHOD:
                    extra_args.append(getattr(event.GetEventObject().FindItemById(event.GetId()), arg))
                elif arg in _PROPERTY:
                    extra_args.append(getattr(event.GetEventObject(), arg)(event.GetId()))
            callback(*extra_args, *callback_args or (), **callback_kwargs or {})

        callback_args = callback_args or ()
        menu.Bind(wx.EVT_MENU, wrapped_callback, item)
    return item


def add_separator() -> wx.MenuItem:
    return add_menu_item('', kind=ITEM.SEPARATOR)


def add_submenu(label: str,
                kind: typing.Optional[int] = None,
                checks: typing.Optional[tuple[str]] = None,
                enable: typing.Optional[bool] = None,
                items: typing.Optional[dict[str, str]] = None,
                callback: typing.Optional[typing.Callable] = None,
                callback_args: typing.Optional[tuple] = None,
                callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                args: typing.Optional[tuple[str]] = None,
                menu: wx.Menu = _MENU) -> wx.MenuItem:
    submenu = wx.Menu()
    checks = checks or ()
    for uid, label_ in items.items():
        item = add_menu_item(label_, kind, uid in checks, label_[0] != '_', uid,
                             callback, callback_args, callback_kwargs, args, submenu)
        if label_[0] == '_':
            item.SetItemLabel(label_[1:])
    submenu_item = menu.AppendSubMenu(submenu, label)
    if enable is not None:
        submenu_item.Enable(enable)
    return submenu_item


# TODO: dump this
def bind_after_close(src_callback: typing.Callable[[...], bool],
                     dest_callback: typing.Callable[[bool, ...], typing.Any],
                     src_callback_args: typing.Optional[tuple] = None,
                     dest_callback_args: typing.Optional[tuple] = None,
                     src_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                     dest_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                     reverse: bool = False) -> typing.Callable:
    def callback():
        state = reverse ^ src_callback(*src_callback_args or (), **src_callback_kwargs or {})
        dest_callback(state, *dest_callback_args or (), **dest_callback_kwargs or {})

    _CALLBACKS.add(callback)
    return callback


def show_balloon(title: str,
                 text: str,
                 icon: int = ICON.NONE) -> bool:
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=icon)


def start_loop(icon_path: str,
               tooltip: typing.Optional[str] = None,
               default_callback: typing.Optional[typing.Callable] = None,
               default_callback_args: typing.Optional[tuple] = None,
               default_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    atexit.register(_destroy)
    if default_callback:
        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK,
                            lambda _: default_callback(*default_callback_args or (), **default_callback_kwargs or {}))
    # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_CLICK, _on_right_click)
    _TASK_BAR_ICON.SetIcon(wx.Icon(icon_path, wx.BITMAP_TYPE_ICO), tooltip)
    _APP.MainLoop()


stop_loop = _APP.ExitMainLoop
