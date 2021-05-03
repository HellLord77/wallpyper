import libs.color
import libs.file
import libs.gui
import libs.request

ok = 200
dummy_generator = (_ for _ in ())

font_style = libs.color.FontStyle
fore_color = libs.color.ForeColor
back_color = libs.color.BackColor
print_color = libs.color.cprint

exists_file = libs.file.exists
copy_file = libs.file.copy
delete_file = libs.file.remove

add_item = libs.gui.add_item
add_separator = libs.gui.add_separator
add_items = libs.gui.add_submenu
sync = libs.gui.bind_after_close
notify = libs.gui.show_balloon
main_loop = libs.gui.main_loop
item = libs.gui.ITEM
icon = libs.gui.ICON

join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve

_start = libs.gui.start_timer
