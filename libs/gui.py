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


# noinspection SpellCheckingInspection
TASK_BAR_ICON = wx.lib.embeddedimage.PyEmbeddedImage(
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

_APP = wx.App()
_MENU = wx.Menu()
_TASK_BAR_ICON = wx.adv.TaskBarIcon()


# noinspection PyUnusedLocal
def _dummy_function(*args: typing.Any,
                    **kwargs: typing.Any) -> None:
    pass


def _on_right_down(_):
    _TASK_BAR_ICON.PopupMenu(_MENU)
    # update


def sync(src, dest, src_property, dest_property):
    pass


def create_menu():
    _MENU.Append(wx.ID_ANY, 'label', 'help')
    # uid: label, kind, bind_func, status_hook
    # uid: self, kind


# noinspection PyDefaultArgument
def add_item(label: str,
             callback: typing.Callable = _dummy_function,
             callback_args: tuple = (),
             callback_kwargs: dict[str, typing.Any] = {}):
    item = _MENU.Append(wx.ID_ANY, label)
    _MENU.Bind(wx.EVT_MENU, lambda _, item_=item: callback(item_, *callback_args, **callback_kwargs), id=item.GetId())
    return item


def show_balloon(title: str,
                 text: str,
                 icon: int = ICON.NONE) -> bool:
    return _TASK_BAR_ICON.ShowBalloon(title, text, flags=icon)


def main_loop(tooltip: str = os.path.basename(sys.argv[0]),
              exit_hook: typing.Callable = _dummy_function):
    _APP.Bind(wx.EVT_END_SESSION, exit_hook)
    _TASK_BAR_ICON.SetIcon(TASK_BAR_ICON.GetIcon(), tooltip)
    _TASK_BAR_ICON.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, _on_right_down)
    # _TASK_BAR_ICON.GetPopupMenu = lambda: _MENU
    _APP.MainLoop()
