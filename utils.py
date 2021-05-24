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

item = libraries.gui.ITEM
icon = libraries.gui.ICON
get_property = libraries.gui.PROPERTY
get_method = libraries.gui.METHOD
add_item = libraries.gui.add_menu_item
add_separator = libraries.gui.add_separator
add_items = libraries.gui.add_submenu
call_after = libraries.gui.bind_call_after
notify = libraries.gui.show_balloon
start = libraries.gui.start_loop
on_exit = libraries.gui.stop_loop

join_url = libraries.request.urljoin
open_url = libraries.request.urlopen
download_url = libraries.request.urlretrieve
