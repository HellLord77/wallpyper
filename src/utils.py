__version__ = '0.0.3'

import os
import webbrowser

import libraries.file
import libraries.functool
import libraries.gui
import libraries.request
import libraries.timer

file_exists = os.path.isfile
exists_dir = os.path.isdir
dir_name = os.path.dirname
file_name = os.path.basename
abs_path = os.path.realpath

open_browser = webbrowser.open

join_path = libraries.file.join
replace_extension = libraries.file.replace_ext
list_dir = libraries.file.iter_dir
copy_file = libraries.file.copy
is_empty_dir = libraries.file.is_empty
make_dirs = libraries.file.make_dir
trim_dir = libraries.file.trim
delete = libraries.file.remove

chain = libraries.functool.chain_ex
reverse = libraries.functool.reversed_ex
dummy_func = libraries.functool.dummy
re_join_path = libraries.functool.re_join
cache = libraries.functool.one_cache
once = libraries.functool.once_run
single = libraries.functool.singleton_run
call_after = libraries.functool.call_after

item = libraries.gui.Item
icon = libraries.gui.Icon
get_property = libraries.gui.Property
get_method = libraries.gui.Method
add_item = libraries.gui.add_menu_item
add_separator = libraries.gui.add_separator
add_items = libraries.gui.create_submenu
add_submenu = libraries.gui.add_submenu
notify = libraries.gui.show_balloon
start = libraries.gui.start_loop
disable = libraries.gui.disable_events
stop = libraries.gui.stop_loop
animate = libraries.gui.start_animation
inanimate = libraries.gui.stop_animation
pause_animation = libraries.gui.disable_animation

status = libraries.request.Status
join_url = libraries.request.urljoin
open_url = libraries.request.urlopen
download_url = libraries.request.download
upload_url = libraries.request.upload

timer = libraries.timer.Timer
thread = libraries.timer.on_thread


def not_implemented(title: str) -> None:
    notify(title, str(NotImplemented))
