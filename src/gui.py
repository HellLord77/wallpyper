import collections
import contextlib
import enum
import functools
import threading
from typing import (Any, Callable, ContextManager, Iterable, Mapping,
                    MutableMapping, MutableSequence, Optional)

import win32
from libs import callables, utils
from win32 import gui

ANIMATION_PATH = ''
GUI = win32.gui.Gui.__new__(win32.gui.Gui)
SYSTEM_TRAY = win32.gui.SystemTray.__new__(win32.gui.SystemTray)
MENU = win32.gui.Menu.__new__(win32.gui.Menu)

_ANIMATED_ICON = utils.MutableBool(True)
_TOOLTIPS: collections.deque[str] = collections.deque()
_MAIN_MENU = object()
_MAIN_MENUS: dict[int, list[gui.Menu]] = {threading.get_ident(): [MENU]}

Event = win32.gui.Event
GuiEvent = win32.gui.GuiEvent
SystemTrayIcon = win32.gui.SystemTrayIcon
MenuItemType = win32.gui.MenuItemType
MenuItemImage = win32.gui.MenuItemImage
MenuItemTooltipIcon = win32.gui.MenuItemTooltipIcon
MenuItemEvent = win32.gui.MenuItemEvent
Gui = win32.gui.Gui
SystemTray = win32.gui.SystemTray
Menu = win32.gui.Menu
MenuItem = win32.gui.MenuItem


class MenuItemAttribute(enum.StrEnum):
    pass


class MenuItemProperty(MenuItemAttribute):
    MENU = win32.gui.MenuItem.get_menu.__name__
    ENABLED = win32.gui.MenuItem.is_enabled.__name__
    CHECKED = win32.gui.MenuItem.is_checked.__name__
    LABEL = win32.gui.MenuItem.get_text.__name__
    SUBMENU = win32.gui.MenuItem.get_submenu.__name__
    POSITION = win32.gui.MenuItem.get_pos.__name__
    UID = win32.gui.MenuItem.get_uid.__name__


class MenuItemMethod(MenuItemAttribute):
    ENABLE = win32.gui.MenuItem.enable.__name__
    SET_ICON = win32.gui.MenuItem.set_icon.__name__
    SET_LABEL = win32.gui.MenuItem.set_text.__name__
    SET_TOOLTIP = win32.gui.MenuItem.set_tooltip.__name__


@contextlib.contextmanager
def set_menu(menu: win32.gui.Menu | win32.gui.MenuItem) -> ContextManager[win32.gui.Menu]:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    thread = threading.get_ident()
    try:
        _MAIN_MENUS[thread].append(menu)
    except KeyError:
        _MAIN_MENUS[thread] = [menu]
    try:
        yield menu
    finally:
        del _MAIN_MENUS[thread][-1]
        if not _MAIN_MENUS[thread]:
            del _MAIN_MENUS[thread]


def set_on_click(menu_item: win32.gui.MenuItem, on_click: Optional[Callable] = None,
                 args: Optional[MenuItemAttribute | Iterable[MenuItemAttribute]] = None, on_thread: bool = True):
    if args is None:
        args = ()
    elif isinstance(args, MenuItemAttribute):
        args = args,

    @functools.wraps(on_click)
    def wrapped(event: Event):
        args_ = []
        for arg in args:
            if isinstance(arg, MenuItemMethod):
                args_.append(getattr(event.control, arg))
            elif isinstance(arg, MenuItemProperty):
                args_.append(getattr(event.control, arg)())
        on_click(*args_)

    if on_thread:
        wrapped = callables.ThreadedCallable(wrapped)
    menu_item.bind(win32.gui.MenuItemEvent.LEFT_UP, wrapped)


def _get_menu(menu: win32.gui.Menu | win32.gui.MenuItem) -> win32.gui.Menu:
    if menu is _MAIN_MENU:
        try:
            menu = _MAIN_MENUS[threading.get_ident()][-1]
        except KeyError:
            menu = next(iter(_MAIN_MENUS.values()))[-1]
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    return menu


def _get_position(position: Optional[int], menu: win32.gui.Menu) -> int:
    if position is None:
        position = menu.get_item_count()
    elif position < 0:
        position += menu.get_item_count()
    return position


def add_menu_item(label: str = '', kind: int = win32.gui.MenuItemType.NORMAL, check: bool = False,
                  enable: bool = True, uid: Optional[int | str] = None, on_click: Optional[Callable] = None,
                  args: Optional[Iterable[MenuItemAttribute]] = None, on_thread: bool = True, position: Optional[int] = None,
                  menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    menu = _get_menu(menu)
    menu_item = menu.insert_item(_get_position(position, menu), label, enable=enable, check=check, type=kind)
    if uid is not None:
        menu_item.set_uid(uid)
    if on_click is not None:
        set_on_click(menu_item, on_click, args, on_thread)
    return menu_item


def get_menu_items(menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> dict[str, win32.gui.MenuItem]:
    menu = _get_menu(menu)
    items = {}
    for item in menu:
        items[item.get_uid()] = item
    return items


def add_separator(position: Optional[int] = None, menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    menu = _get_menu(menu)
    return add_menu_item(kind=win32.gui.MenuItemType.SEPARATOR, position=position, menu=menu)


def add_submenu(label: str, enable: bool = True, uid: Optional[int | str] = None,
                position: Optional[int] = None, icon: Optional[int | str] = None,
                menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    menu = _get_menu(menu)
    item = menu.insert_item(_get_position(position, menu), label, submenu=win32.gui.Menu(), enable=enable)
    if uid is not None:
        item.set_uid(uid)
    if icon is not None:
        item.set_icon(icon)
    return item


def add_menu_item_check(label: str, mapping: MutableMapping[str, bool], key: str,
                        enable: bool = True, on_click: Optional[Callable] = None, position: Optional[int] = None,
                        menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    if on_click is None:
        wrapped = mapping.__setitem__
    else:
        @functools.wraps(on_click)
        def wrapped(key_: str, checked: bool):
            mapping[key_] = checked
            return on_click(checked)
    return add_menu_item(label, win32.gui.MenuItemType.CHECK, mapping[key], enable, on_click=functools.partial(
        wrapped, key), args=(MenuItemProperty.CHECKED,), position=position, menu=menu)


def _get_submenu(label_or_submenu_item: str | win32.gui.MenuItem, enable: bool = True,
                 position: Optional[int] = None, icon: Optional[int | str] = None,
                 menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    if isinstance(label_or_submenu_item, str):
        label_or_submenu_item = add_submenu(label_or_submenu_item, position=position, menu=menu)
    if enable is not None:
        label_or_submenu_item.enable(enable)
    if icon is not None:
        label_or_submenu_item.set_icon(icon)
    return label_or_submenu_item


def add_submenu_check(label_or_submenu_item: str | win32.gui.MenuItem,
                      labels: Iterable[str] | Mapping[int | str, str], min_max: tuple[Optional[int], Optional[int]],
                      mapping: MutableMapping[str, MutableSequence[bool | int | str]], key: str, enable: bool = True,
                      on_click: Optional[Callable] = None, args: Optional[Iterable[MenuItemAttribute]] = None,
                      position: Optional[int] = None, icon: Optional[int | str] = None,
                      menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    submenu_item = _get_submenu(label_or_submenu_item, enable, position, icon, menu)

    def wrapped():
        unchecked_checked = [], []
        for index_, item in enumerate(submenu):
            item.enable(True)
            checked = item.is_checked()
            if mapped:
                uid_ = item.get_uid()
                try:
                    val.remove(uid_)
                except ValueError:
                    pass
                if checked:
                    val.append(uid_)
            else:
                val[index_] = checked
            unchecked_checked[checked].append(item)
        count_checked = len(unchecked_checked[1])
        for count, items in zip(min_max, reversed(unchecked_checked)):
            if count_checked == count:
                for item_ in items:
                    item_.enable(False)

    if on_click is None:
        on_click_ = wrapped
        args = ()
    else:
        @functools.wraps(on_click)
        def on_click_(uid_: int | str, *args_):
            wrapped()
            return on_click(uid_, *args_)

        args = MenuItemProperty.UID, *(() if args is None else args)
    val = mapping[key]
    submenu = submenu_item.get_submenu()
    mapped = isinstance(labels, Mapping)
    for uid, label in labels.items() if mapped else enumerate(labels):
        add_menu_item(label, win32.gui.MenuItemType.CHECK, uid in val if mapped else val[
            uid], uid=uid, on_click=on_click_, args=args, menu=submenu)
    wrapped()
    return submenu_item


def add_submenu_radio(label_or_submenu_item: str | win32.gui.MenuItem, items: Mapping[str, str],
                      mapping: MutableMapping[str, str], key: str, enable: bool = True,
                      on_click: Optional[Callable] = None, args: Optional[Iterable[MenuItemAttribute]] = None,
                      position: Optional[int] = None, icon: Optional[int | str] = None,
                      menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> win32.gui.MenuItem:
    submenu_item = _get_submenu(label_or_submenu_item, enable, position, icon, menu)
    if on_click is None:
        wrapped = mapping.__setitem__
    else:
        @functools.wraps(on_click)
        def wrapped(key_: str, uid: str, *args_):
            mapping[key_] = uid
            return on_click(uid, *args_)
    val = mapping[key]
    on_click_ = functools.partial(wrapped, key)
    args = MenuItemProperty.UID, *(() if args is None else args)
    submenu = submenu_item.get_submenu()
    for uid_, label in items.items():
        add_menu_item(label, win32.gui.MenuItemType.RADIO, val == uid_, uid=uid_,
                      on_click=on_click_, args=args, menu=submenu)
    return submenu_item


def get_menu_item_by_uid(uid: int | str, recursive: bool = True,
                         menu: win32.gui.Menu | win32.gui.MenuItem = _MAIN_MENU) -> Optional[win32.gui.MenuItem]:
    menu = _get_menu(menu)
    for submenu in menu:
        if uid == submenu.get_uid():
            return submenu
        elif recursive and (submenu := submenu.get_submenu()):
            if menu_item := get_menu_item_by_uid(uid, recursive, submenu):
                return menu_item


def init(name: str):
    GUI.__init__(name)
    SYSTEM_TRAY.__init__()
    MENU.__init__()


def start_loop(icon: str, tooltip: Optional[str] = None, callback: Optional[Callable[[], Any]] = None):
    SYSTEM_TRAY.set_icon(icon)
    SYSTEM_TRAY.set_tooltip(tooltip)
    if callback is not None:
        SYSTEM_TRAY.bind(win32.gui.SystemTrayEvent.LEFT_DOUBLE,
                         functools.wraps(callback)(lambda _: callback()))
    SYSTEM_TRAY.bind(win32.gui.SystemTrayEvent.RIGHT_DOWN, lambda _: MENU.show())
    # GUI.bind(win32.gui.GuiEvent.QUERY_END_SESSION, stop_loop)  # TODO fix shutdown
    SYSTEM_TRAY.show()
    GUI.mainloop()


def stop_loop(*_):
    GUI.exit_mainloop()


def disable_events():
    SYSTEM_TRAY.unbind(win32.gui.SystemTrayEvent.LEFT_DOUBLE)
    SYSTEM_TRAY.unbind(win32.gui.SystemTrayEvent.RIGHT_DOWN)


def _animate_icon():
    animate = False
    try:
        tooltip = _TOOLTIPS[-1]
    except IndexError:
        tooltip = GUI.get_name()
    else:
        animate = True
    SYSTEM_TRAY.set_tooltip(tooltip)
    if animate and _ANIMATED_ICON:
        if not SYSTEM_TRAY.is_animated():
            SYSTEM_TRAY.start_animation(ANIMATION_PATH)
    else:
        SYSTEM_TRAY.stop_animation()


def enable_animated_icon(enable: bool = True):
    _ANIMATED_ICON.set(enable)
    _animate_icon()


@contextlib.contextmanager
def try_animate_icon(tooltip: Optional[str] = None, force: bool = False) -> ContextManager[None]:
    if tooltip is None:
        tooltip = GUI.get_name()
    _TOOLTIPS.append(GUI.get_name() if tooltip is None else tooltip)
    enable_animated_icon() if force else _animate_icon()
    try:
        yield
    finally:
        try:
            _TOOLTIPS.remove(tooltip)
        except ValueError:
            pass
        else:
            _animate_icon()


def enable_menuitem_icon(enable: bool = True, *, __set_icon=win32.gui.MenuItem.set_icon):
    win32.gui.MenuItem.set_icon = __set_icon if enable else lambda *_, **__: True
