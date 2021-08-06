__version__ = '0.0.3'

import os

import libraries.file
import libraries.functool
import libraries.gui
import libraries.request
import libraries.timer

exists_file = os.path.isfile

join_path = libraries.file.join
copy_file = libraries.file.copy
is_empty_dir = libraries.file.is_empty
make_dirs = libraries.file.make_dir
trim_dir = libraries.file.trim
delete = libraries.file.remove

cache = libraries.functool.one_cache
once = libraries.functool.once_run
single = libraries.functool.one_run

item = libraries.gui.Item
icon = libraries.gui.Icon
get_property = libraries.gui.Property
get_method = libraries.gui.Method
add_item = libraries.gui.add_menu_item
add_separator = libraries.gui.add_separator
add_items = libraries.gui.add_submenu
notify = libraries.gui.show_balloon
start = libraries.gui.start_loop
disable = libraries.gui.disable
stop = libraries.gui.stop_loop
animate = libraries.gui.start_animation
inanimate = libraries.gui.stop_animation

status = libraries.request.Status
join_url = libraries.request.urljoin
open_url = libraries.request.urlopen
download_url = libraries.request.download
upload_url = libraries.request.upload

timer = libraries.timer.Timer
thread = libraries.timer.on_thread
