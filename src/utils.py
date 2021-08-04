__version__ = '0.0.3'

import os

import libs.file
import libs.functool
import libs.gui
import libs.request
import libs.timer

exists_file = os.path.isfile

join_path = libs.file.join
copy_file = libs.file.copy
delete_file = libs.file.remove
delete_dir = libs.file.remove_tree

cache = libs.functool.one_cache
once = libs.functool.once_run
single = libs.functool.one_run

item = libs.gui.Item
icon = libs.gui.Icon
get_property = libs.gui.Property
get_method = libs.gui.Method
add_item = libs.gui.add_menu_item
add_separator = libs.gui.add_separator
add_items = libs.gui.add_submenu
notify = libs.gui.show_balloon
start = libs.gui.start_loop
disable = libs.gui.disable
stop = libs.gui.stop_loop
animate = libs.gui.start_animation
inanimate = libs.gui.stop_animation

status = libs.request.Status
join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.download
upload_url = libs.request.upload

timer = libs.timer.Timer
thread = libs.timer.on_thread
