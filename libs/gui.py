import os
import sys
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


class PROPERTY:
    IS_CHECKED = 'IsChecked'
    IS_ENABLED = 'IsEnabled'
    GET_UID = 'GetHelpString'


class METHOD:
    SET_LABEL = 'SetItemLabel'


_APP = wx.App()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()
# noinspection SpellCheckingInspection
_ICON = wx.lib.embeddedimage.PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAnhJREFUOI11k79KXEEUxr/5c+/evenEQhA0gooYOxvRx'
    b'QfwFSLBQrAJeQFBYmNrSLBb8SmyInYWCcg2uqYJiZXg3SYr7t7d+X9SXO+NCWTgMAdmvt+Z+c4Mu729fROCe2eMWyKimHPOAIAxhn8HEeFpzTImbu'
    b'JYfmTfbm7aURTNJ/X6iyRJOOcCAFWAYiYQoQgEaKVpNBzm2pjvcqTUUlKvR0IIHkIAUSEuo6xKREVOBM45k1GU9vv9V9w5F0spORGhBPwvjDF4v7+'
    b'PnZ0dSCm58z6WgQIjCvD+z105FygtKE9BIBwcHOD15iamp6bgvQcRMe6dh3MeIQSEEGCMQav1GScnJ2g0Guh2uwCAr1++YjAY4OX0dLXX+wBeJL46'
    b'/uHhIWZmZrC6uoqFhQVMTEyAMYbT01Osra2hvGqhc+DOuQoQQkCr1cLc3Bza7TaWl5chhADnHJeXl1hZWakApUaWAM45GGNYX19HCAHn5+eYnJxEs'
    b'9lEnudIkgTj4+Ow1lYA5xxkmZRt293dhXMO9/f3aDabqNVqODs7Q5Zl8N5XwrKwdNbBWvvkf2F9u91Go9EAgaC1xtXVFRYXF2GtrcTOFTqujYYxBs'
    b'YYWGuQ5zmur6+xvb0NrTS01uh0Opidna32PQ9ujIFSCt1uF1tbW9jb28PGxgY451BKYTQa4e7uDkdHR7i4uIDWBVQpBWst2PHxsRkbG5NpmrI4jhF'
    b'FEaSUEEJUvgCojLPWwliDfJBTr/fgZK/3q0PAvPc+TdOUO+cghPgLUD7lEjAcDunx8XH48PDwQ2ZZ95NS+u1oOFqq1aJYyohJKau2Pv/KZResta7f'
    b'7//MsuzDb1Mp5IMPSMlnAAAAAElFTkSuQmCC'
)
_CALLBACKS = set()
_PROPERTIES = PROPERTY.__dict__.values()
_METHODS = METHOD.__dict__.values()


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
            wrapped_callback_args = []
            if args:
                for arg in args:
                    if arg in _PROPERTIES:
                        wrapped_callback_args.append(getattr(event.GetEventObject(), arg)(event.GetId()))
                    elif arg in _METHODS:
                        wrapped_callback_args.append(getattr(event.GetEventObject().FindItemById(event.GetId()), arg))
            if callback_args:
                wrapped_callback_args.extend(callback_args)
            callback(*wrapped_callback_args, **callback_kwargs or {})

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


def main_loop(tooltip: str = os.path.basename(sys.argv[0]),
              default_callback: typing.Optional[typing.Callable] = None,
              default_callback_args: typing.Optional[tuple] = None,
              default_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
              exit_callback: typing.Optional[typing.Callable] = None,
              exit_callback_args: typing.Optional[tuple] = None,
              exit_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
    _TASK_BAR_ICON.SetIcon(_ICON.GetIcon(), tooltip)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, _on_right_click)
    if default_callback:
        _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK,
                            lambda _: default_callback(*default_callback_args or (), **default_callback_kwargs or {}))
        # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
        # TODO: catch shutdown event correctly
        if exit_callback:
            _APP.Bind(wx.EVT_END_SESSION,
                      lambda _: exit_callback(*exit_callback_args or (), **exit_callback_kwargs or {}))
        _APP.MainLoop()


def destroy() -> None:
    wx.CallAfter(_MENU.Destroy)
    wx.CallAfter(_TASK_BAR_ICON.Destroy)
