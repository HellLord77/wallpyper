import libs.color
import libs.file
import libs.request

true = 'true'
false = 'false'
ok = 200

dummy_generator = (_ for _ in ())

font_style = libs.color.FontStyle
fore_color = libs.color.ForeColor
back_color = libs.color.BackColor
print_color = libs.color.cprint

exists_file = libs.file.exists
copy_file = libs.file.copy
delete_file = libs.file.remove

join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve
