__version__ = '0.0.2'

import os

import libraries.file
import libraries.functool
import libraries.gui
import libraries.request
import libraries.timer

join_path = os.path.join
exists_file = os.path.isfile

copy_file = libraries.file.copy
delete_file = libraries.file.remove
delete_dir = libraries.file.remove_tree

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
on_exit = libraries.gui.stop_loop
animate = libraries.gui.start_animation
inanimate = libraries.gui.stop_animation

status = libraries.request.Status
join_url = libraries.request.urljoin
open_url = libraries.request.urlopen
download_url = libraries.request.download
upload_url = libraries.request.upload

timer = libraries.timer.Timer
thread = libraries.timer.on_thread
kill = libraries.timer.kill_all
