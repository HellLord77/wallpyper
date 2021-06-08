from libraries import cache
from libraries import color
from libraries import file
from libraries import gui
from libraries import request

ok = 200

cache = cache.one_cache

font_style = color.FontStyle
fore_color = color.ForeColor
back_color = color.BackColor
print_color = color.cprint

join_path = file.join
exists_file = file.exists
copy_file = file.copy
delete_file = file.remove
delete_dir = file.remove_tree

item = gui.Item
icon = gui.Icon
get_property = gui.Property
get_method = gui.Method
add_item = gui.add_menu_item
add_separator = gui.add_separator
add_items = gui.add_submenu
notify = gui.show_balloon
start = gui.start_loop
on_exit = gui.stop_loop
animate = gui.start_animation
inanimate = gui.stop_animation

join_url = request.urljoin
open_url = request.urlopen
download_url = request.urlretrieve
