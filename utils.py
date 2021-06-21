from libraries import file
from libraries import functool
from libraries import gui
from libraries import request

join_path = file.join
exists_file = file.exists
copy_file = file.copy
delete_file = file.remove
delete_dir = file.remove_tree

cache = functool.one_cache
once = functool.one_run
single = functool.singleton
is_running = functool.running

item = gui.Item
icon = gui.Icon
get_property = gui.Property
get_method = gui.Method
add_item = gui.add_menu_item
add_separator = gui.add_separator
add_items = gui.add_submenu
notify = gui.show_balloon
start = gui.start_loop
disable = gui.disable
on_exit = gui.stop_loop
animate = gui.start_animation
inanimate = gui.stop_animation

status = request.Status
join_url = request.urljoin
open_url = request.urlopen
download_url = request.download
upload_url = request.upload
