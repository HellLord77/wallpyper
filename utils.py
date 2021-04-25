import libs.debug
import libs.file
import libs.request

blue_color = libs.debug.COLORS['blue']
green_color = libs.debug.COLORS['green']
red_color = libs.debug.COLORS['red']
reset_color = libs.debug.RESET
print_color = libs.debug.log

exists_file = libs.file.exists
copy_file = libs.file.copy
delete_file = libs.file.remove

join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve
