import collections
import contextlib
import functools
import threading
from typing import Any, Callable, ContextManager, Iterable, Mapping, MutableMapping, Optional

import win32

ANIMATION_PATH = ''
GUI = win32.gui.Gui.__new__(win32.gui.Gui)
SYSTEM_TRAY = win32.gui.SystemTray.__new__(win32.gui.SystemTray)
MENU = win32.gui.Menu.__new__(win32.gui.Menu)

_ENABLE_ANIMATION = True
_TOOLTIPS: collections.deque[str] = collections.deque()
_ANIMATIONS: collections.deque[tuple[str, str]] = collections.deque()
_MAIN_MENU = [MENU]

GuiEvent = win32.gui.GuiEvent
SystemTrayIcon = win32.gui.SystemTrayIcon
MenuItemType = win32.gui.MenuItemType
MenuItemImage = win32.gui.MenuItemImage
MenuItemTooltipIcon = win32.gui.MenuItemTooltipIcon
Gui = win32.gui.Gui
SystemTray = win32.gui.SystemTray
Menu = win32.gui.Menu
MenuItem = win32.gui.MenuItem


class _Arg(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        cls._values = set(getattr(cls, var) for var in dir(cls) if not var.startswith('_'))
        return cls

    def __contains__(cls, item):
        return item in cls._values


class Method(metaclass=_Arg):
    ENABLE = win32.gui.MenuItem.enable.__name__
    SET_LABEL = win32.gui.MenuItem.set_text.__name__


class Property(metaclass=_Arg):
    CHECKED = win32.gui.MenuItem.is_checked.__name__
    ENABLED = win32.gui.MenuItem.is_enabled.__name__
    UID = win32.gui.MenuItem.get_uid.__name__
    LABEL = win32.gui.MenuItem.get_text.__name__


@contextlib.contextmanager
def set_main_menu(menu: win32.gui.Menu | win32.gui.MenuItem) -> ContextManager[win32.gui.Menu]:  # TODO cythonize (__defaults__)
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    defaults_bk = {}
    for func in globals().values():
        if defaults := getattr(func, '__defaults__', None):
            defaults_bk[func] = func.__defaults__
            func.__defaults__ = tuple(menu if default is _MAIN_MENU[-1] else default for default in defaults)
    _MAIN_MENU.append(menu)
    try:
        yield menu
    finally:
        for func, defaults in defaults_bk.items():
            func.__defaults__ = defaults
        _MAIN_MENU.pop()


def _get_wrapper(on_click: Callable, menu_args: Iterable[str], args: Iterable,
                 kwargs: Mapping[str, Any], set_state: bool, on_thread: bool, pre_menu_args: bool) -> Callable:
    @functools.wraps(on_click)
    def wrapper(_: int, menu_item: win32.gui.MenuItem):
        if set_state:
            menu_item.enable(False)
        args_ = [] if pre_menu_args else list(args)
        for menu_arg in menu_args:
            if menu_arg in Method:
                args_.append(getattr(menu_item, menu_arg))
            elif menu_arg in Property:
                args_.append(getattr(menu_item, menu_arg)())
        if pre_menu_args:
            args_.extend(args)
        try:
            on_click(*args_, **kwargs)
        finally:
            if set_state:
                menu_item.enable()

    if not on_thread:
        return wrapper

    @functools.wraps(wrapper)
    def wrapper_thread(event: int, menu_item: win32.gui.MenuItem) -> threading.Thread:
        thread = threading.Thread(target=wrapper, name=f'{__name__}-{on_click.__name__}', args=(event, menu_item))
        thread.start()
        return thread

    return wrapper_thread


def set_on_click(menu_item: win32.gui.MenuItem, callback: Optional[Callable] = None,
                 menu_args: Optional[Iterable[str]] = None, args: Optional[Iterable] = None,
                 kwargs: Optional[Mapping[str, Any]] = None, on_thread: bool = True, change_state: bool = True,
                 pre_menu_args: bool = True):
    menu_item.bind(win32.gui.MenuItemEvent.LEFT_UP, _get_wrapper(
        callback, () if menu_args is None else menu_args, () if args is None else args,
        {} if kwargs is None else kwargs, change_state, on_thread, pre_menu_args))


def add_menu_item(label: str = '', kind: int = win32.gui.MenuItemType.NORMAL, check: bool = False, enable: bool = True,
                  uid: Optional[int | str] = None, on_click: Optional[Callable] = None,
                  menu_args: Optional[Iterable[str]] = None, args: Optional[Iterable] = None,
                  kwargs: Optional[Mapping[str, Any]] = None, on_thread: bool = True, change_state: bool = True,
                  position: Optional[int] = None, pre_menu_args: bool = True,
                  menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> win32.gui.MenuItem:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    menu_item = menu.insert_item(menu.get_item_count() if position is None else position, label, enable=enable, check=check, type=kind)
    if uid is not None:
        menu_item.set_uid(uid)
    if on_click is not None:
        set_on_click(menu_item, on_click, menu_args, args, kwargs, on_thread, change_state, pre_menu_args)
    return menu_item


def get_menu_items(menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> dict[str, win32.gui.MenuItem]:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    items = {}
    for item in menu:
        items[item.get_uid()] = item
    return items


def add_separator(position: Optional[int] = None, menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> win32.gui.MenuItem:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    return add_menu_item(kind=win32.gui.MenuItemType.SEPARATOR, position=position, menu=menu)


def add_submenu(label: str, enable: bool = True, uid: Optional[int | str] = None,
                position: Optional[int] = None, icon: Optional[int | str] = None,
                menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> win32.gui.MenuItem:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    item = menu.insert_item(menu.get_item_count() if position is None else position, label, submenu=win32.gui.Menu(), enable=enable)
    if uid is not None:
        item.set_uid(uid)
    if icon is not None:
        item.set_icon(icon)
    return item


def add_mapped_menu_item(label: str, mapping: MutableMapping[str, bool],
                         key: str, enable: bool = True, on_click: Optional[Callable] = None,
                         args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None,
                         position: Optional[int] = None, menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> win32.gui.MenuItem:
    if on_click is None:
        on_click_ = mapping.__setitem__
    else:
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}

        @functools.wraps(on_click)
        def on_click_(key_: str, checked: bool):
            mapping[key_] = checked
            return on_click(checked, *args, **kwargs)
    return add_menu_item(label, win32.gui.MenuItemType.CHECK, mapping[key], enable, on_click=on_click_,
                         menu_args=(Property.CHECKED,), args=(key,), position=position, pre_menu_args=False, menu=menu)


def add_mapped_submenu(label_or_submenu_item: str | win32.gui.MenuItem, items: Mapping[str, str],
                       mapping: MutableMapping[str, str], key: str, enable: bool = True,
                       uid: Optional[int | str] = None, on_click: Optional[Callable] = None,
                       args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None,
                       position: Optional[int] = None, menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> win32.gui.MenuItem:
    submenu_item = add_submenu(label_or_submenu_item, position=position, menu=menu) if isinstance(
        label_or_submenu_item, str) else label_or_submenu_item
    if uid is not None:
        submenu_item.set_uid(uid)
    if enable is not None:
        submenu_item.enable(enable)
    if on_click is None:
        on_click_ = mapping.__setitem__
    else:
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}

        @functools.wraps(on_click)
        def on_click_(key_: str, uid_: str):
            mapping[key_] = uid_
            return on_click(uid_, *args, **kwargs)
    submenu = submenu_item.get_submenu()
    for index, (uid__, label_) in enumerate(items.items(), 1):
        add_menu_item(label_, win32.gui.MenuItemType.RADIO, mapping[key] == uid__, uid=uid__, on_click=on_click_,
                      menu_args=(Property.UID,), args=(key,), pre_menu_args=False, menu=submenu)
    return submenu_item


def get_menu_item_by_uid(uid: int | str, recursive: bool = True,
                         menu: win32.gui.Menu | win32.gui.MenuItem = MENU) -> Optional[win32.gui.MenuItem]:
    if isinstance(menu, win32.gui.MenuItem):
        menu = menu.get_submenu()
    menu_: win32.gui.MenuItem
    for menu_ in menu:
        if uid == menu_.get_uid():
            return menu_
        elif recursive and (submenu := menu_.get_submenu()):
            if menu_item := get_menu_item_by_uid(uid, recursive, submenu):
                return menu_item


def init(name: str):
    GUI.__init__(name)
    SYSTEM_TRAY.__init__()
    MENU.__init__()


def start_loop(path: str, tooltip: Optional[str] = None, callback: Optional[Callable] = None,
               args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
    SYSTEM_TRAY.set_icon(path)
    SYSTEM_TRAY.set_tooltip(tooltip)
    if callback is not None:
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}

        @functools.wraps(callback)
        def wrapper(_: int, __: win32.gui.SystemTray):
            callback(*args, **kwargs)

        SYSTEM_TRAY.bind(win32.gui.SystemTrayEvent.LEFT_DOUBLE, wrapper)
    SYSTEM_TRAY.bind(win32.gui.SystemTrayEvent.RIGHT_DOWN, lambda _, __: MENU.show())
    GUI.bind(win32.gui.GuiEvent.QUERY_END_SESSION, stop_loop)  # TODO fix shutdown
    SYSTEM_TRAY.show()
    GUI.mainloop()


def stop_loop(*_):
    GUI.exit_mainloop()


def disable_events():
    SYSTEM_TRAY.unbind(win32.gui.SystemTrayEvent.LEFT_DOUBLE)
    SYSTEM_TRAY.unbind(win32.gui.SystemTrayEvent.RIGHT_DOWN)
    GUI.unbind(win32.gui.GuiEvent.DISPLAY_CHANGE)


def _animate():
    animate_ = False
    try:
        tooltip = _TOOLTIPS[-1]
    except IndexError:
        tooltip = GUI.get_name()
    else:
        animate_ = True
    SYSTEM_TRAY.set_tooltip(tooltip)
    if animate_ and _ENABLE_ANIMATION:
        if not SYSTEM_TRAY.is_animated():
            SYSTEM_TRAY.start_animation(ANIMATION_PATH)
    else:
        SYSTEM_TRAY.stop_animation()


def enable_animation(enable: bool = True):
    global _ENABLE_ANIMATION
    _ENABLE_ANIMATION = enable
    _animate()


@contextlib.contextmanager
def animate(tooltip: Optional[str] = None) -> ContextManager[None]:
    if tooltip is None:
        tooltip = GUI.get_name()
    _TOOLTIPS.append(GUI.get_name() if tooltip is None else tooltip)
    _animate()
    try:
        yield
    finally:
        try:
            _TOOLTIPS.remove(tooltip)
        except ValueError:
            pass
        else:
            _animate()
