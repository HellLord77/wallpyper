__version__ = '0.0.4'

import os
import sys
import webbrowser

import libs.file
import libs.functool
import libs.gui
import libs.request
import libs.timer

max_int = sys.maxsize

file_exists = os.path.isfile
exists_dir = os.path.isdir
dir_name = os.path.dirname
file_name = os.path.basename
abs_path = os.path.realpath

open_browser = webbrowser.open

join_path = libs.file.join
replace_extension = libs.file.replace_ext
list_dir = libs.file.iter_dir
copy_file = libs.file.copy
is_empty_dir = libs.file.is_empty
make_dirs = libs.file.make_dir
trim_dir = libs.file.trim
delete = libs.file.remove

Int = libs.functool.Int
TimeDelta = libs.functool.TimeDelta
try_any = libs.functool.any_ex
enquote = libs.functool.enquote
reverse = libs.functool.reversed_ex
dummy_func = libs.functool.dummy
re_join_path = libs.functool.re_join
cache = libs.functool.one_cache
once = libs.functool.once_run
single = libs.functool.singleton_run
call_after = libs.functool.call_after
call_before = libs.functool.call_before

item = libs.gui.Item
icon = libs.gui.Icon
get_property = libs.gui.Property
get_method = libs.gui.Method
add_item = libs.gui.add_menu_item
add_separator = libs.gui.add_separator
add_submenu = libs.gui.add_submenu
notify = libs.gui.show_balloon
start = libs.gui.start_loop
disable = libs.gui.disable_events
stop = libs.gui.stop_loop
animate = libs.gui.start_animation
inanimate = libs.gui.stop_animation
pause_animation = libs.gui.disable_animation

status = libs.request.Status
join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.download
upload_url = libs.request.upload

timer = libs.timer.Timer
thread = libs.timer.on_thread


def not_implemented(title: str) -> None:
    notify(title, str(NotImplemented))
