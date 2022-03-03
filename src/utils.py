__version__ = '0.0.4'

import os

import libs.functool
import libs.gui
import libs.paths
import libs.request
import libs.timer

path_exists = os.path.isfile
dir_exists = os.path.isdir
get_dir = os.path.dirname
get_filename = os.path.basename
abspath = os.path.realpath
split_filename = os.path.splitext

join_path = libs.paths.join
replace_extension = libs.paths.replace_ext
list_dir = libs.paths.iter_dir
copy_file = libs.paths.copy
is_empty_dir = libs.paths.is_empty
make_dirs = libs.paths.make_dir
trim_dir = libs.paths.trim
delete = libs.paths.remove

Int = libs.functool.MutableInt
List = libs.functool.PointedList
Dict = libs.functool.FrozenDict
Wallpaper = libs.functool.RemoteFile
try_any = libs.functool.any_ex
enquote = libs.functool.enquote
reverse = libs.functool.reversed_ex
dummy_func = libs.functool.pass_ex
re_join_path = libs.functool.re_join
cache = libs.functool.one_cache
once = libs.functool.once_run
single = libs.functool.singleton_run
call_after = libs.functool.call_after
call_before = libs.functool.call_before

item = libs.gui.Item
icon = libs.gui.Icon
get_property = libs.gui.Property
set_property = libs.gui.Method
on_item_click = libs.gui.on_menu_item_click
add_item = libs.gui.add_menu_item
add_synced_item = libs.gui.add_mapped_menu_item
add_synced_items = libs.gui.add_mapped_submenu
clear_menu = libs.gui.remove_menu_items
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

status = libs.request.Status
join_url = libs.request.join
query_url = libs.request.query
encode_url = libs.request.encode
open_url = libs.request.open
download_url = libs.request.download
upload_url = libs.request.upload

Timer = libs.timer.Timer
thread = libs.timer.on_thread


def not_implemented(title: str):
    notify(title, str(NotImplemented))
