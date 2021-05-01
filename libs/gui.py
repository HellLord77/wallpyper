import os
import sys
import typing

import wx
import wx.adv
import wx.lib.embeddedimage

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

SLEEP = 0.1


class ITEM:
    SEPARATOR = -1
    NORMAL = 0
    CHECK = 1
    RADIO = 2
    SUBMENU = 3


class WINDOW:
    BUTTON = 0
    DIR = 1


class ICON:
    ERROR = 512
    EXCLAMATION = 256
    INFORMATION = 2048
    MASK = 790272
    NONE = 262144
    QUESTION = 1024


def _on_right_click(_: wx.Event) -> None:
    _TASK_BAR_ICON.PopupMenu(_MENU)


def add_item(label: str,
             kind: int = ITEM.NORMAL,
             callback: typing.Optional[typing.Callable] = None,
             callback_args: typing.Optional[tuple] = None,
             callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
             menu: wx.Menu = _MENU) -> wx.MenuItem:
    item = menu.Append(wx.ID_ANY, label, kind=kind)
    if callback:
        menu.Bind(wx.EVT_MENU, lambda _: callback(*callback_args or (), **callback_kwargs or {}), id=item.GetId())
    return item


def sync(src_callback: typing.Callable[[...], bool],
         dest_callback: typing.Callable[[bool, ...], typing.Any],
         src_callback_args: typing.Optional[tuple] = None,
         dest_callback_args: typing.Optional[tuple] = None,
         src_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         dest_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         reverse: bool = False) -> None:
    _MENU.Bind(wx.EVT_UPDATE_UI,
               lambda _: dest_callback(reverse ^ src_callback(*src_callback_args or (), **src_callback_kwargs or {}),
                                       *dest_callback_args or (), **dest_callback_kwargs or {}))


def show_balloon(title: str,
                 text: str,
                 icon: int = ICON.NONE) -> bool:
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=icon)


def main_loop(tooltip: str = os.path.basename(sys.argv[0]),
              exit_hook: typing.Optional[typing.Callable] = None):
    _APP.Bind(wx.EVT_END_SESSION, exit_hook)
    _TASK_BAR_ICON.SetIcon(_ICON.GetIcon(), tooltip)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, _on_right_click)
    # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
    _APP.MainLoop()
