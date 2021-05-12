import libs.color
import libs.file
import libs.gui
import libs.request

ok = 200

font_style = libs.color.FontStyle
fore_color = libs.color.ForeColor
back_color = libs.color.BackColor
print_color = libs.color.cprint

exists_file = libs.file.exists
copy_file = libs.file.copy
delete_file = libs.file.remove
delete_dir = libs.file.remove_tree

item = libs.gui.ITEM
icon = libs.gui.ICON
get_property = libs.gui.PROPERTY
get_method = libs.gui.METHOD
add_item = libs.gui.add_menu_item
add_separator = libs.gui.add_separator
add_items = libs.gui.add_submenu
call_after = libs.gui.bind_after_close
notify = libs.gui.show_balloon
start = libs.gui.start_loop
on_exit = libs.gui.stop_loop

join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve
