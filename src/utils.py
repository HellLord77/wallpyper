__version__ = '0.0.4'

import libs.files
import libs.gui
import libs.request

Wallpaper = libs.files.File

item = libs.gui.Item
icon = libs.gui.Icon
get_property = libs.gui.Property
set_property = libs.gui.Method
on_item_click = libs.gui.on_menu_item_click
add_item = libs.gui.add_menu_item
add_synced_item = libs.gui.add_mapped_menu_item
add_synced_items = libs.gui.add_mapped_submenu
add_separator = libs.gui.add_separator
add_menu = libs.gui.add_submenu
get_item = libs.gui.get_menu_item_by_uid
notify = libs.gui.show_balloon
start = libs.gui.start_loop
disable = libs.gui.disable_events
stop = libs.gui.stop_loop
animate = libs.gui.start_animation
inanimate = libs.gui.stop_animation
pause_animation = libs.gui.disable_animation


def not_implemented(title: str):
    notify(title, str(NotImplemented))
