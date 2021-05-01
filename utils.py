import libs.color
import libs.file
import libs.gui
import libs.request

true = 'true'
false = 'false'
ok = 200

dummy_function = lambda *arg, **kwargs: None
dummy_generator = (_ for _ in ())

font_style = libs.color.FontStyle
fore_color = libs.color.ForeColor
back_color = libs.color.BackColor
print_color = libs.color.cprint

exists_file = libs.file.exists
copy_file = libs.file.copy
delete_file = libs.file.remove

add_menu_item = libs.gui.add_item
sync = libs.gui.sync
notify = libs.gui.show_balloon
main_loop = libs.gui.main_loop
item_kind = libs.gui.ITEM
icon_kind = libs.gui.ICON

join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve
