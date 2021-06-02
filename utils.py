import libraries.color
import libraries.file
import libraries.gui
import libraries.request

ok = 200

font_style = libraries.color.FontStyle
fore_color = libraries.color.ForeColor
back_color = libraries.color.BackColor
print_color = libraries.color.cprint

exists_file = libraries.file.exists
copy_file = libraries.file.copy
delete_file = libraries.file.remove
delete_dir = libraries.file.remove_tree

item = libraries.gui.Item
icon = libraries.gui.Icon
get_property = libraries.gui.Property
get_method = libraries.gui.Method
add_item = libraries.gui.add_menu_item
add_separator = libraries.gui.add_separator
add_items = libraries.gui.add_submenu
notify = libraries.gui.show_balloon
start = libraries.gui.start_loop
on_exit = libraries.gui.stop_loop
animate = libraries.gui.start_animation
inanimate = libraries.gui.stop_animation

join_url = libraries.request.urljoin
open_url = libraries.request.urlopen
download_url = libraries.request.urlretrieve
