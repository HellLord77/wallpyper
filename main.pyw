import configparser
import contextlib
import functools
import os
import sys
import threading
import typing

import wx
import wx.adv

# 639-1
import languages.en
import libraries.debug
import libraries.singleton
import libraries.thread
import modules.wallhaven
# sys.platform
import platforms.win32
import utils

NAME = 'wallpyper'
PLATFORM = platforms.win32

LANGUAGES = (languages.en,)
LANGUAGE = LANGUAGES[0]
MODULES = (modules.wallhaven,)
MODULE = MODULES[0]
DEFAULT_CONFIG: dict[str, typing.Union[str, int, float, bool]] = {'auto_change': False,
                                                                  'change_interval': 3600,
                                                                  'auto_save': False,
                                                                  'save_dir': os.path.join(PLATFORM.PICTURES_DIR, NAME),
                                                                  'notify': False,
                                                                  'auto_start': False,
                                                                  'save_config': False}

CONFIG_PATH = os.path.join('E:\\Projects\\wxWallhaven\\config.ini')  # os.path.join(PLATFORM.APPDATA_DIR, f'{NAME}.ini')
TEMP_DIR = os.path.join(PLATFORM.TEMP_DIR, NAME)
INTERVALS = {'300': '5 Minute',
             '900': '15 Minute',
             '1800': '30 Minute',
             '3600': '1 Hour',
             '10800': '3 Hour',
             '21600': '6 Hour'}

CHANGING = False
SAVING = False
CONFIG = {}


class Change:
    CALLBACK = None
    TIMER = None


# 0.0.1

DEFAULT_FRAME_STYLE = wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.FRAME_TOOL_WINDOW
configs = {
    'auto_change': False,
    'change_interval': 3600000,
    'auto_save': False,
    'save_dir': os.path.join(PLATFORM.PICTURES_DIR, NAME),
    'use_api_key': True,
    'auto_ratio': True,
    'auto_start': False
}
paramsEX = {
    'apikey': None,
    'q': None,
    'categories': '111',
    'purity': '100',
    'sorting': 'date_added',
    'order': 'desc',
    'topRange': '1M',
    'atleast': None,
    'resolutions': None,
    'ratios': None,
    'colors': None,
    'page': None,
    'seed': None
}
categories = {
    '0': 'General',
    '1': 'Anime',
    '2': 'People'
}
purity = {
    '0': 'SFW',
    '1': 'Sketchy',
    '2': 'NSFW'
}
sorting = {
    'date_added': 'Date Added',
    'relevance': 'Relevance',
    'random': 'Random',
    'views': 'Views',
    'favorites': 'Favorites',
    'toplist': 'Toplist',
    'hot': 'Hot'
}
order = {
    'desc': 'Descending',
    'asc': 'Ascending'
}
topRange = {
    '1d': 'Last Day',
    '3d': 'Last 3 Days',
    '1w': 'Last Week',
    '1M': 'Last Month',
    '3M': 'Last 3 Months',
    '6M': 'Last 6 Months',
    '1y': 'Last Year'
}
atleast = [
    'None',
    '_5:4', '1280x1024', '1600x1280', '1920x1536', '2560x2048', '3840x3072',
    '_4:3', '1280x960', '1600x1200', '1920x1440', '2560x1920', '3840x2880',
    '_16:10', '1280x800', '1600x1000', '1920x1200', '2560x1600', '3840x2400',
    '_16:9', '1280x720', '1600x900', '1920x1080', '2560x1440', '3840x2160',
    '_Ultrawide', '2560x1080', '3440x1440', '3840x1600'
]
atleast = {resolution: resolution for resolution in atleast}
resolutions = dict(atleast)
del resolutions['None']
ratios = [
    '_Square', '1x1', '3x2', '4x3', '5x4',
    '_Portrait', '9x16', '10x16', '9x18',
    '_Ultrawide', '21x9', '32x9', '48x9',
    '_Wide', '16x9', '16x10'
]
ratios = {ratio: ratio for ratio in ratios}
colors = [
    'None',
    '#660000', '#990000', '#cc0000', '#cc3333', '#ea4c88',
    '#993399', '#663399', '#333399', '#0066cc', '#0099cc',
    '#66cccc', '#77cc33', '#669900', '#336600', '#666600',
    '#999900', '#cccc33', '#ffff00', '#ffcc33', '#ff9900',
    '#ff6600', '#cc6633', '#996633', '#663300', '#000000',
    '#999999', '#cccccc', '#ffffff', '#424153'
]
colors = {color: color for color in colors}


def create_item(menu, label, func):
    item = wx.MenuItem(menu, wx.ID_ANY, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


def create_submenu_items(item_submenu, dict_, kind):
    submenu = item_submenu.GetSubMenu()
    if kind == wx.ITEM_RADIO:
        append_checkable = submenu.AppendRadioItem
    else:
        append_checkable = submenu.AppendCheckItem
    for id, label in dict_.items():
        kind = id[0]
        if kind == '_':
            submenu_item = append_checkable(wx.ID_ANY, label[1:])
            submenu_item.Enable(False)
        elif kind == '#':
            item_color = wx.Colour()
            item_color.Set(id)
            submenu_item = wx.MenuItem(submenu, wx.ID_ANY, label, id, wx.ITEM_RADIO)
            submenu_item.SetBackgroundColour(item_color)
            submenu.Append(submenu_item)
        else:
            append_checkable(wx.ID_ANY, label, id)


def get_param_submenu_items_id(item_submenu):
    id = item_submenu.GetHelp()
    param = paramsEX[id]
    submenu = item_submenu.GetSubMenu()
    submenu_items = submenu.GetMenuItems()
    return param, submenu_items, id


def parse_params_1(item_submenu):
    param, submenu_items = get_param_submenu_items_id(item_submenu)[:-1]
    for index, state in enumerate(param):
        submenu_items[index].Check(int(state))


def parse_params_2(item_submenu):
    param, submenu_items = get_param_submenu_items_id(item_submenu)[:-1]
    for submenu_item in submenu_items:
        if submenu_item.GetHelp() == param:
            submenu_item.Check(True)
            break


def parse_params_3(item_submenu):
    param, submenu_items = get_param_submenu_items_id(item_submenu)[:-1]
    for submenu_item in submenu_items:
        id = submenu_item.GetHelp()
        state = id in param if (id and param) else False
        submenu_item.Check(state)


def update_params_1(item_submenu):
    param = ''
    submenu_items, id = get_param_submenu_items_id(item_submenu)[1:]
    for submenu_item in submenu_items:
        state = submenu_item.IsChecked()
        param += str(int(state))
    paramsEX[id] = param


def update_params_2(item_submenu):
    submenu_items, id = get_param_submenu_items_id(item_submenu)[1:]
    for submenu_item in submenu_items:
        if submenu_item.IsChecked():
            param = submenu_item.GetHelp()
            param = param.replace('#', '')
            paramsEX[id] = None if param == 'None' else param
            break


def update_params_3(item_submenu):
    submenu_items, id = get_param_submenu_items_id(item_submenu)[1:]
    param = ''
    for submenu_item in submenu_items:
        if submenu_item.IsChecked():
            dim = submenu_item.GetHelp()
            param += f'{dim},'
    param = param or None
    paramsEX[id] = param


def get_optimal_ratio():
    display_resolution = wx.DisplaySize()
    display_ratio = display_resolution[0] / display_resolution[1]
    d0 = 1024
    optimal_ratio = next(iter(ratios.values()))
    for ratio in ratios:
        if ratio[0] != '_':
            w, h = ratio.split('x')
            aspect_ratio = int(w) / int(h)
            d1 = abs(display_ratio - aspect_ratio)
            if d1 <= d0:
                d0 = d1
                optimal_ratio = ratio
    return optimal_ratio


def modify_search_query(textctrl, loop):
    search_query = textctrl.GetLineText(0)
    paramsEX['q'] = search_query or None
    loop.Exit()


def on_modify_search_query(_):
    def func(_):
        return modify_search_query(textctrl, loop)

    frame = wx.Frame(None, wx.ID_ANY, 'Search Query', style=DEFAULT_FRAME_STYLE)
    frame.Bind(wx.EVT_CLOSE, lambda _: loop.Exit())
    panel = wx.Panel(frame, wx.ID_ANY)
    staticbox = wx.StaticBox(panel, wx.ID_ANY, f'Current Search Query: {paramsEX["q"]}')
    sizer = wx.StaticBoxSizer(staticbox)
    textctrl = wx.TextCtrl(panel, wx.ID_ANY, (paramsEX['q'] or ''), style=wx.TE_PROCESS_ENTER)
    textctrl.Bind(wx.EVT_TEXT_ENTER, func)
    sizer.Add(textctrl, wx.EXPAND)
    button = wx.Button(panel, wx.ID_ANY, 'Modify Search Query')
    button.Bind(wx.EVT_BUTTON, func)
    sizer.Add(button)
    panel.SetSizer(sizer)
    sizer.SetSizeHints(frame)
    show_frame(frame)
    button.SetDefault()
    loop = wx.GUIEventLoop()
    loop.Run()
    frame.Destroy()


def show_frame(frame):
    w0, h0 = wx.ClientDisplayRect()[2:]
    w, h = frame.GetSize()
    frame.SetPosition((w0 - w, h0 - h))
    frame.Show()
    frame.Raise()


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super().__init__()
        self.icon = wx.Icon('icon.icon')
        self.SetIcon(self.icon, NAME)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_change)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.on_right_down)
        app.Bind(wx.EVT_END_SESSION, self.on_exit)
        self.save_path = configs['save_dir']
        self.change_interval = configs['change_interval']
        self.bk_categories = paramsEX['categories']
        self.bk_purity = paramsEX['purity']
        self.bk_atleast_1 = self.bk_atleast_2 = paramsEX['atleast']
        self.bk_resolutions_1 = self.bk_resolutions_2 = paramsEX['resolutions']
        self.bk_ratios = paramsEX['ratios']
        self.func = lambda progress: self.change_wallpaper.SetItemLabel(f'Change Wallpaper ({progress:03}%)')
        self.thread = threading.Thread(target=self.change)
        self.display_ratio = get_optimal_ratio()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_change, self.timer)
        self.menu = wx.Menu()
        self.change_wallpaper = create_item(self.menu, 'Change Wallpaper', self.on_change)
        self.auto_change = self.menu.AppendCheckItem(wx.ID_ANY, 'Auto Change Wallpaper')
        self.auto_change.Check(configs['auto_change'])
        self.menu.Bind(wx.EVT_MENU, self.on_auto_change, id=self.auto_change.GetId())
        self.item_submenu_interval = self.menu.AppendSubMenu(wx.Menu(), 'Auto Change Interval')
        create_submenu_items(self.item_submenu_interval, INTERVALS, wx.ITEM_RADIO)
        self.menu.AppendSeparator()
        self.save_wallpaper = create_item(self.menu, 'Save Wallpaper', self.on_save)
        self.auto_save = self.menu.AppendCheckItem(wx.ID_ANY, 'Auto Save Wallpaper')
        self.auto_save.Check(configs['auto_save'])
        create_item(self.menu, 'Modify Save Folder', self.on_modify_save_folder)
        self.menu.AppendSeparator()
        self.use_api_key = self.menu.AppendCheckItem(wx.ID_ANY, 'Use API Key')
        self.use_api_key.Check(bool(configs['use_api_key'] and paramsEX['apikey']))
        create_item(self.menu, 'Modify API Key', self.on_modify_api_key)
        self.remove_api_key = create_item(self.menu, 'Remove API Key', self.on_remove_api_key)
        self.remove_api_key.Enable(bool(paramsEX['apikey']))
        self.menu.AppendSeparator()
        create_item(self.menu, 'Modify Search Query', on_modify_search_query)
        self.item_submenu_categories = self.menu.AppendSubMenu(wx.Menu(), 'Category', 'categories')
        create_submenu_items(self.item_submenu_categories, categories, wx.ITEM_CHECK)
        self.item_submenu_purity = self.menu.AppendSubMenu(wx.Menu(), 'Purity', 'purity')
        create_submenu_items(self.item_submenu_purity, purity, wx.ITEM_CHECK)
        self.item_submenu_colors = self.menu.AppendSubMenu(wx.Menu(), 'Color', 'colors')
        create_submenu_items(self.item_submenu_colors, colors, wx.ITEM_RADIO)
        self.menu.AppendSeparator()
        self.item_submenu_sorting = self.menu.AppendSubMenu(wx.Menu(), 'Sort By', 'sorting')
        create_submenu_items(self.item_submenu_sorting, sorting, wx.ITEM_RADIO)
        self.item_submenu_order = self.menu.AppendSubMenu(wx.Menu(), 'Sort Order', 'order')
        create_submenu_items(self.item_submenu_order, order, wx.ITEM_RADIO)
        self.item_submenu_topRange = self.menu.AppendSubMenu(wx.Menu(), 'Top List Range', 'topRange')
        create_submenu_items(self.item_submenu_topRange, topRange, wx.ITEM_RADIO)
        self.menu.AppendSeparator()
        self.auto_ratio = self.menu.AppendCheckItem(wx.ID_ANY, f'Auto Ratio ({self.display_ratio})')
        self.auto_ratio.Check(configs['auto_ratio'])
        self.menu.Bind(wx.EVT_MENU, self.on_auto_ratio, id=(self.auto_ratio.GetId()))
        self.item_submenu_ratios = self.menu.AppendSubMenu(wx.Menu(), 'Resolution Ratio', 'ratios')
        create_submenu_items(self.item_submenu_ratios, ratios, wx.ITEM_CHECK)
        self.item_submenu_atleast = self.menu.AppendSubMenu(wx.Menu(), 'Least Resolution', 'atleast')
        create_submenu_items(self.item_submenu_atleast, atleast, wx.ITEM_RADIO)
        self.item_submenu_resolutions = self.menu.AppendSubMenu(wx.Menu(), 'Exact Resolution', 'resolutions')
        create_submenu_items(self.item_submenu_resolutions, resolutions, wx.ITEM_CHECK)
        self.menu.AppendSeparator()
        self.autorun = self.menu.AppendCheckItem(wx.ID_ANY, 'Auto Startup')
        self.autorun.Check(configs['auto_start'])
        self.save_configuration = self.menu.AppendCheckItem(wx.ID_ANY, 'Save Configuration')
        self.save_configuration.Check(utils.exists_file(CONFIG_PATH))
        self.menu.Bind(wx.EVT_MENU, self.on_auto_startup, id=self.autorun.GetId())
        create_item(self.menu, 'Exit Wallhaven', self.on_exit)
        self.parse_interval()
        self.parse_params()
        self.update_popup_menu()
        self.on_auto_change()
        self.on_auto_ratio()
        self.on_auto_startup()
        if 'change' in sys.argv:
            self.on_change()

    def update_popup_menu(self):
        if paramsEX['apikey']:
            self.use_api_key.Enable(True)
        else:
            self.use_api_key.Enable(False)
            self.use_api_key.Check(False)
        nsfw = self.item_submenu_purity.GetSubMenu().GetMenuItems()[(-1)]
        if self.use_api_key.IsChecked():
            nsfw.Enable(True)
        else:
            nsfw.Enable(False)
            nsfw.Check(False)
        submenu_sorting = self.item_submenu_sorting.GetSubMenu()
        state_1 = submenu_sorting.FindItemById(submenu_sorting.FindItem('Toplist')).IsChecked()
        self.item_submenu_topRange.Enable(state_1)
        atleast = paramsEX['atleast']
        if self.bk_atleast_1 != atleast:
            if atleast:
                paramsEX['resolutions'] = None
                parse_params_3(self.item_submenu_resolutions)
        elif self.bk_resolutions_1 != paramsEX['resolutions']:
            paramsEX['atleast'] = 'None'
            parse_params_2(self.item_submenu_atleast)

    def parse_interval(self):
        submenu_interval = self.item_submenu_interval.GetSubMenu()
        intervals = submenu_interval.GetMenuItems()
        for interval in intervals:
            if int(interval.GetHelp()) == self.change_interval:
                interval.Check(True)
                break

    def update_interval(self):
        submenu_interval = self.item_submenu_interval.GetSubMenu()
        intervals = submenu_interval.GetMenuItems()
        for interval in intervals:
            if interval.IsChecked():
                change_interval = int(interval.GetHelp())
                restart = self.change_interval != change_interval
                self.change_interval = change_interval
                self.on_auto_change() if restart else None
                break

    def parse_params(self):
        parse_params_1(self.item_submenu_categories)
        parse_params_1(self.item_submenu_purity)
        parse_params_2(self.item_submenu_sorting)
        parse_params_2(self.item_submenu_order)
        parse_params_2(self.item_submenu_topRange)
        parse_params_2(self.item_submenu_atleast)
        parse_params_3(self.item_submenu_resolutions)
        parse_params_3(self.item_submenu_ratios)
        parse_params_2(self.item_submenu_colors)

    def update_params(self):
        update_params_1(self.item_submenu_categories)
        update_params_1(self.item_submenu_purity)
        update_params_2(self.item_submenu_sorting)
        update_params_2(self.item_submenu_order)
        update_params_2(self.item_submenu_topRange)
        update_params_2(self.item_submenu_atleast)
        update_params_3(self.item_submenu_resolutions)
        update_params_3(self.item_submenu_ratios)
        update_params_2(self.item_submenu_colors)

    def fix_categories_purity(self):
        if not int(paramsEX['categories']):
            paramsEX['categories'] = self.bk_categories
            parse_params_1(self.item_submenu_categories)
        if not int(paramsEX['purity']):
            paramsEX['purity'] = self.bk_purity
            parse_params_1(self.item_submenu_purity)

    def on_right_down(self, _):
        self.bk_atleast_1 = paramsEX['atleast']
        self.bk_resolutions_1 = paramsEX['resolutions']
        self.PopupMenu(self.menu)
        self.update_interval()
        self.update_params()
        self.update_popup_menu()

    def on_change(self, _=None):
        if not self.thread.is_alive():
            self.thread.start()
            self.thread = threading.Thread(target=self.change)

    def on_auto_change(self, _=None):
        state = self.auto_change.IsChecked()
        self.item_submenu_interval.Enable(state)
        self.timer.Start(self.change_interval) if state else self.timer.Stop()
        if self.autorun.IsChecked():
            self.on_auto_startup()

    def on_save(self, _):
        self.save_wallpaper.Enable(False)
        path = PLATFORM.get_wallpaper_path()
        name = os.path.basename(path)
        save_path = os.path.join(self.save_path, name)
        saved = utils.copy_file(path, save_path)
        if not saved:
            cache_name = next(os.walk(PLATFORM.WALLPAPER_DIR))[2][0]
            save_path_2 = os.path.join(self.save_path, cache_name)
            saved = utils.copy_file(path, save_path_2)
            if not saved:
                cache_path = os.path.join(PLATFORM.WALLPAPER_DIR, cache_name)
                saved = utils.copy_file(cache_path, save_path)
                if not saved:
                    saved = utils.copy_file(cache_path, save_path_2)
        self.save_wallpaper.Enable(True)
        return saved

    def on_modify_save_folder(self, _=None):
        save_path = self.save_path
        while not os.path.isdir(save_path):
            if save_path:
                save_path = os.path.dirname(save_path)

        frame = wx.Frame(None, wx.ID_ANY, 'Save Folder', style=DEFAULT_FRAME_STYLE)
        frame.Bind(wx.EVT_CLOSE, lambda _: loop.Exit())
        panel = wx.Panel(frame, wx.ID_ANY)
        staticbox = wx.StaticBox(panel, wx.ID_ANY, f'Current Save Folder: {self.save_path}')
        sizer = wx.StaticBoxSizer(staticbox)
        dirpickerctrl = wx.DirPickerCtrl(panel, wx.ID_ANY, save_path, 'Browse for Folder')
        sizer.Add(dirpickerctrl, wx.EXPAND)
        button = wx.Button(panel, wx.ID_ANY, 'Modify Save Folder')
        button.Bind(wx.EVT_BUTTON, lambda _: self.modify_save_folder(dirpickerctrl, loop))
        sizer.Add(button)
        panel.SetSizer(sizer)
        sizer.SetSizeHints(frame)
        show_frame(frame)
        button.SetDefault()
        loop = wx.GUIEventLoop()
        loop.Run()
        frame.Destroy()

    def on_modify_api_key(self, _):
        frame = wx.Frame(None, wx.ID_ANY, 'API Key', style=DEFAULT_FRAME_STYLE)
        frame.Bind(wx.EVT_CLOSE, lambda _: loop.Exit())
        frame.CreateStatusBar()
        frame.SetStatusText('[#] Get API Key from https://wallhaven.cc/settings/account')
        panel = wx.Panel(frame, wx.ID_ANY)
        staticbox = wx.StaticBox(panel, wx.ID_ANY, f'Current API Key: {paramsEX["apikey"]}')
        sizer = wx.StaticBoxSizer(staticbox)
        button = wx.Button(panel, wx.ID_ANY, 'Fetch API Key From Clipboard && Modify API Key After Verifying')
        button.Bind(wx.EVT_BUTTON, lambda _: self.modify_api_key(frame, button, loop))
        sizer.Add(button)
        panel.SetSizer(sizer)
        sizer.SetSizeHints(frame)
        show_frame(frame)
        loop = wx.GUIEventLoop()
        loop.Run()
        frame.Destroy()

    def on_remove_api_key(self, _):
        paramsEX['apikey'] = None
        self.remove_api_key.Enable(False)

    def on_auto_ratio(self, _=None):
        state = self.auto_ratio.IsChecked()
        enable = not state
        self.item_submenu_atleast.Enable(enable)
        self.item_submenu_resolutions.Enable(enable)
        self.item_submenu_ratios.Enable(enable)
        if state:
            self.bk_atleast_2 = paramsEX['atleast']
            self.bk_resolutions_2 = paramsEX['resolutions']
            self.bk_ratios = paramsEX['ratios']
            paramsEX['atleast'] = 'None'
            paramsEX['resolutions'] = None
            paramsEX['ratios'] = f'{self.display_ratio},'
        else:
            paramsEX['atleast'] = self.bk_atleast_2
            paramsEX['resolutions'] = self.bk_resolutions_2
            paramsEX['ratios'] = self.bk_ratios
        parse_params_2(self.item_submenu_atleast)
        parse_params_3(self.item_submenu_resolutions)
        parse_params_3(self.item_submenu_ratios)
        update_params_2(self.item_submenu_atleast)

    def on_auto_startup(self, _=None):
        path = os.path.realpath(sys.argv[0])
        if self.autorun.IsChecked():
            PLATFORM.register_autorun(NAME, path, 'change' if self.auto_change.IsChecked() else '')
        else:
            PLATFORM.unregister_autorun(NAME)

    def on_exit(self, _):
        if self.save_configuration.IsChecked():
            self.save_config()
        else:
            utils.delete_file(CONFIG_PATH)
        utils.delete_dir(TEMP_DIR)
        wx.CallAfter(self.Destroy)

    def change(self):
        self.change_wallpaper.Enable(False)
        self.change_wallpaper.SetItemLabel('Change Wallpaper (000%)')
        self.fix_categories_purity()
        MODULE.CONFIG.update(paramsEX)
        change_wallpaper(self.func)
        self.change_wallpaper.SetItemLabel('Change Wallpaper')
        self.change_wallpaper.Enable(True)

    def modify_save_folder(self, dirpickerctrl, loop):
        save_path = dirpickerctrl.GetPath()
        while not os.path.isdir(save_path):
            if save_path:
                save_path = os.path.dirname(save_path)

        if save_path:
            self.save_path = save_path
            loop.Exit()

    def modify_api_key(self, frame, button, loop):
        button.Disable()
        frame.Update()
        frame.SetStatusText('[#] Verifying API Key')
        text_data = wx.TextDataObject()
        wx.TheClipboard.GetData(text_data)
        api_key = text_data.GetText()
        if MODULE.authenticate(api_key):
            paramsEX['apikey'] = api_key
            self.remove_api_key.Enable(True)
            loop.Exit()
        else:
            frame.SetStatusText(f'[#] Invalid API Key')
            app.Yield()
            button.Enable()
            button.SetFocus()

    def save_config(self):
        configs.update({'auto_change': self.auto_change.IsChecked(),
                        'change_interval': self.change_interval,
                        'auto_save': self.auto_save.IsChecked(),
                        'save_dir': self.save_path,
                        'auto_ratio': self.auto_ratio.IsChecked(),
                        'auto_start': self.autorun.IsChecked()})
        save_config()


# 0.0.2

def _load_config(config_parser: configparser.ConfigParser,
                 section: str,
                 config: dict[str, typing.Union[str, int, float, bool]],
                 default_config: dict[str, typing.Union[str, int, float, bool]],
                 get_converted: dict[type, typing.Callable[[str, str, ...], typing.Any]]) -> bool:
    loaded = True
    config.update(default_config)
    if config_parser.has_section(section):
        for option, value in default_config.items():
            if config_parser.has_option(section, option):
                try:
                    # noinspection PyArgumentList
                    config[option] = get_converted[type(value)](section, option)
                except TypeError:
                    loaded = False
            else:
                loaded = False
    else:
        loaded = False
    return loaded


def load_config() -> bool:
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_PATH)
    get_converted = {
        str: config_parser.get,
        int: config_parser.getint,
        float: config_parser.getfloat,
        bool: config_parser.getboolean
    }
    loaded = _load_config(config_parser, NAME, CONFIG, DEFAULT_CONFIG, get_converted)
    for module in MODULES:
        loaded = _load_config(config_parser, module.NAME, module.CONFIG,
                              module.DEFAULT_CONFIG, get_converted) and loaded
    return loaded


def save_config() -> bool:
    config_parser = configparser.ConfigParser()
    config_parser[NAME] = CONFIG
    for module in MODULES:
        with contextlib.suppress(TypeError):
            config_parser[module.NAME] = module.CONFIG
    with open(CONFIG_PATH, 'w') as file:
        config_parser.write(file)
    return utils.exists_file(CONFIG_PATH)


def update_config(value: typing.Any,
                  key: str) -> None:
    CONFIG.__setitem__(key, value)


def change_wallpaper(callback: typing.Optional[typing.Callable[[int], typing.Any]] = None) -> bool:
    global CHANGING
    if not CHANGING:
        CHANGING = True
        animated = utils.animate('resources/wedges.gif', LANGUAGE.CHANGING)
        # noinspection PyBroadException
        try:
            url = MODULE.get_next_url()
        except Exception:
            url = ''
        name = os.path.basename(url)
        temp_path = os.path.join(TEMP_DIR, name)
        save_path = os.path.join(CONFIG['save_dir'], name)
        utils.download_url(url, temp_path, chunk_count=100, callback=callback)
        changed = PLATFORM.set_wallpaper(temp_path, save_path)
        if CONFIG['auto_save'] and not utils.copy_file(temp_path, save_path) and changed:
            save_wallpaper()
        CHANGING = False
        if animated:
            utils.inanimate()
        return changed
    return False


def save_wallpaper() -> bool:
    global SAVING
    if not SAVING:
        SAVING = True
        animated = utils.animate('resources/wedges.gif', LANGUAGE.SAVING)
        path = PLATFORM.get_wallpaper_path()
        name = os.path.basename(path)
        cache_name = next(os.walk(PLATFORM.WALLPAPER_DIR))[2][0]
        saved = utils.copy_file(path, CONFIG['save_dir'], name, cache_name)
        if not saved:
            saved = utils.copy_file(os.path.join(PLATFORM.WALLPAPER_DIR, cache_name),
                                    CONFIG['save_dir'], name, cache_name)
        SAVING = False
        if animated:
            utils.inanimate()
        return saved
    return False


def on_change() -> bool:
    Change.CALLBACK(0)
    changed = change_wallpaper(Change.CALLBACK)
    Change.CALLBACK(100)
    if not changed and CONFIG['notify']:
        utils.notify(LANGUAGE.CHANGE, LANGUAGE.FAILED_CHANGING)  # TODO: retry count (?)
    return changed


def on_auto_change(is_checked: bool, change_interval: typing.Optional[wx.MenuItem] = None) -> None:
    CONFIG['auto_change'] = is_checked
    if change_interval:
        change_interval.Enable(is_checked)
    Change.TIMER.start(CONFIG['change_interval']) if is_checked else Change.TIMER.stop()


def on_change_interval(interval: str) -> None:
    CONFIG['change_interval'] = int(interval)
    on_auto_change(CONFIG['auto_change'])


def on_save() -> bool:
    if not save_wallpaper():
        if CONFIG['notify']:
            utils.notify(LANGUAGE.SAVE, LANGUAGE.FAILED_SAVING)
        return False
    return True


def _on_modify_save():
    # TODO: show folder picker
    ...


def on_auto_start(is_checked: bool) -> bool:
    CONFIG['auto_start'] = is_checked
    if is_checked:
        args = set(('change',) if CONFIG['auto_change'] else ())
        return PLATFORM.register_autorun(NAME, os.path.realpath(sys.argv[0]), *args)
    else:
        return PLATFORM.unregister_autorun(NAME)


def on_save_config(is_checked: bool) -> None:
    CONFIG['save_config'] = is_checked
    save_config() if is_checked else utils.delete_file(CONFIG_PATH)


def create_menu() -> None:
    change = utils.add_item(LANGUAGE.CHANGE, callback=libraries.thread.start, callback_args=(on_change,))

    @functools.wraps(change.SetItemLabel)
    def wrapper(progress: int) -> None:
        if progress == 100:
            change.SetItemLabel(f'{LANGUAGE.CHANGING}')
        else:
            change.SetItemLabel(f'{LANGUAGE.CHANGING} ({progress:02}%)')

    Change.CALLBACK = wrapper
    Change.TIMER = libraries.thread.Timer(CONFIG['change_interval'], on_change)
    change_interval = utils.add_items(LANGUAGE.CHANGE_INTERVAL, utils.item.RADIO, (str(CONFIG['change_interval']),),
                                      CONFIG['auto_change'], INTERVALS, on_change_interval,
                                      default_args=(utils.get_property.GET_UID,))
    utils.add_item(LANGUAGE.AUTO_CHANGE, utils.item.CHECK, CONFIG['auto_change'], callback=on_auto_change,
                   callback_args=(change_interval,), default_args=(utils.get_property.IS_CHECKED,), pos=1)
    utils.add_separator()
    utils.add_item(LANGUAGE.SAVE, callback=libraries.thread.start, callback_args=(on_save,))
    utils.add_item(LANGUAGE.AUTO_SAVE, utils.item.CHECK, CONFIG['auto_save'], callback=update_config,
                   callback_args=('auto_save',), default_args=(utils.get_property.IS_CHECKED,))
    utils.add_item(LANGUAGE.MODIFY_SAVE, callback=_on_modify_save)
    utils.add_separator()
    MODULE.create_menu()  # TODO: separate left click menu (?)
    utils.add_separator()
    utils.add_item(LANGUAGE.NOTIFY, utils.item.CHECK, CONFIG['notify'], callback=update_config,
                   callback_args=('notify',), default_args=(utils.get_property.IS_CHECKED,))
    utils.add_item(LANGUAGE.AUTO_START, utils.item.CHECK, CONFIG['auto_start'], callback=on_auto_start,
                   default_args=(utils.get_property.IS_CHECKED,))
    utils.add_item(LANGUAGE.SAVE_CONFIG, utils.item.CHECK, CONFIG['save_config'], callback=on_save_config,
                   default_args=(utils.get_property.IS_CHECKED,))
    utils.add_item(LANGUAGE.EXIT, callback=utils.on_exit)


def start() -> None:
    if 'debug' in sys.argv:
        libraries.debug.init('languages', 'libraries', 'modules', 'platforms')
    libraries.singleton.init(NAME, 'wait' in sys.argv, print, print, print, ('Crash',), ('Wait',), ('Exit',))
    load_config()
    create_menu()
    on_auto_change(CONFIG['auto_change'])
    if 'change' in sys.argv:
        libraries.thread.start(on_change)
    on_auto_start(CONFIG['auto_start'])
    on_save_config(CONFIG['save_config'])
    utils.start('resources/pinwheel.png', NAME, libraries.thread.start, (on_change,))


def stop() -> None:
    Change.TIMER.stop()
    on_auto_start(CONFIG['auto_start'])
    on_save_config(CONFIG['save_config'])
    utils.delete_dir(TEMP_DIR)


if __name__ == '__main__':
    start()
    stop()
    sys.exit()
    # 0.0.1
    app = wx.App()
    TaskBarIcon()
    app.MainLoop()
    sys.exit()
