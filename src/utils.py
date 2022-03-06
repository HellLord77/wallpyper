__version__ = '0.0.4'

import os

import libs.files
import libs.gui
import libs.misc
import libs.request

path_exists = os.path.isfile
dir_exists = os.path.isdir
get_dir = os.path.dirname
get_filename = os.path.basename
abspath = os.path.realpath
split_filename = os.path.splitext

Wallpaper = libs.files.File
join_path = libs.files.join
set_ext = libs.files.replace_ext
list_dir = libs.files.iter_dir
copy_file = libs.files.copy
is_empty_dir = libs.files.is_empty
make_dirs = libs.files.make_dir
trim_dir = libs.files.trim
delete = libs.files.remove

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

try_any = libs.misc.any_ex
enquote = libs.misc.enquote
reverse = libs.misc.reversed_ex
dummy_func = libs.misc.pass_ex
re_join_path = libs.misc.re_join
cache = libs.misc.one_cache
once = libs.misc.once_run
single = libs.misc.singleton_run
call_after = libs.misc.call_after
call_before = libs.misc.call_before

strip_url = libs.request.strip
join_url = libs.request.join
query_url = libs.request.query
encode_url = libs.request.encode
open_url = libs.request.open


def not_implemented(title: str):
    notify(title, str(NotImplemented))
