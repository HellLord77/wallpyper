import functools
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import ImageFile
from . import Source

URL_BASE = 'https://wallpaperswide.com'
URL_SEARCH = request.join_url(URL_BASE, 'search')
URL_FILTER = request.join_url(URL_BASE, 'setfilter.html')
URL_DOWNLOAD = request.join_url(URL_BASE, 'download')

CONFIG_ORDER = '_ratios'
CONFIG_QUALITY = '_quality'
CONFIG_GALLERY = 'gallery'
CONFIG_SEARCH = 'q'
CONFIG_RATIO = 'flt_ratio'
CONFIG_RESOLUTION = 'flt_res'
CONFIG_CATEGORY = 'category'
CONFIG_RESOLUTIONS = 'resolution'

ORDER = (
    'Wide 16:10', 'Wide 5:3', 'UltraWide 21:9', 'UltraWide 24:10', 'HD 16:9',
    'UHD 16:9', 'Standard 4:3', 'Standard 5:4', 'Standard 3:2',
    'Smartphone 16:9', 'Smartphone 3:2', 'Smartphone 5:3', 'Tablet 1:1',
    'iPad 1/2/Mini', 'Mobile VGA 4:3', 'Mobile WVGA 5:3', 'Mobile HVGA 3:2',
    'Mobile WXGA 16:9', 'Mobile XGA 5:4', 'Dual Wide 16:10', 'Dual Wide 5:3',
    'Dual HD 16:9', 'Dual UHD 16:9', 'Dual Standard 4:3', 'Dual Standard 5:4',
    'Dual Standard 3:2', 'Triple Wide 16:10', 'Triple Wide 5:3',
    'Triple HD 16:9', 'Triple UHD 16:9', 'Triple Standard 4:3',
    'Triple Standard 5:4', 'Triple Standard 3:2')
QUALITIES = 'low', 'high'
GALLERIES = (
    '', 'top', 'latest', 'top_downloaded', 'top_favorite',
    'random', 'search', 'category', 'resolution')
RATIOS = '', 'wide', 'hd', 'std', 'mobi', 'x2', 'x3'
RESOLUTIONS = (
    '', '0', '960x600', '1152x720', '1280x800', '1440x900', '1680x1050',
    '1920x1200', '2560x1600', '2880x1800', '3840x2400', '5120x3200',
    '7680x4800', '1', '800x480', '1280x768', '2', '2560x1080', '3440x1440',
    '5120x2160', '3', '3840x1600', '4', '960x540', '1024x576', '1280x720',
    '1366x768', '1600x900', '1920x1080', '2048x1152', '2400x1350', '2560x1440',
    '2880x1620', '3554x1999', '5', '3840x2160', '5120x2880', '7680x4320', '6',
    '800x600', '1024x768', '1152x864', '1280x960', '1400x1050', '1440x1080',
    '1600x1200', '1680x1260', '1920x1440', '2048x1536', '2560x1920',
    '2800x2100', '3200x2400', '4096x3072', '6400x4800', '7', '1280x1024',
    '2560x2048', '3750x3000', '5120x4096', '8', '1152x768', '1440x960',
    '1920x1280', '2000x1333', '2160x1440', '2736x1824', '3000x2000', '9',
    '540x960', '720x1280', '1080x1920', '1440x2560', '320x480', '640x960',
    '768x1152', '480x800', '768x1280', '1024x1024', '1280x1280', '2048x2048',
    '2560x2560', '2732x2732', '3840x3840', '240x320', '480x640', '600x800',
    '320x240', '640x480', '800x600', '240x400', '480x800', '400x240', '800x480',
    '320x480', '640x960', '480x320', '960x640', '272x480', '360x640', '480x854',
    '480x272', '640x360', '854x480', '176x220', '220x176', '10', '1920x600',
    '2304x720', '2560x800', '2880x900', '3360x1050', '3840x1200', '5120x1600',
    '5600x1800', '7680x2400', '10240x3200', '15360x4800', '11', '1600x480',
    '2560x768', '12', '1920x540', '2048x576', '2560x720', '2732x768',
    '3200x900', '3840x1080', '4096x1152', '4800x1350', '5120x1440', '5760x1620',
    '7108x1999', '13', '7680x2160', '10240x2880', '15360x4320', '14',
    '1600x600', '2048x768', '2304x864', '2560x960', '2800x1050', '2880x1080',
    '3200x1200', '3360x1260', '3840x1440', '4096x1536', '5120x1920',
    '5600x2100', '6400x2400', '8192x3072', '12800x4800', '15', '2560x1024',
    '5120x2048', '7500x3000', '10240x4096', '16', '2304x768', '2880x960',
    '3840x1280', '4000x1333', '4320x1440', '5472x1824', '6000x2000', '17',
    '3840x800', '4320x900', '5040x1050', '5760x1200', '7680x1600', '8640x1800',
    '11520x2400', '15360x3200', '23040x4800', '18', '2400x480', '3840x768',
    '19', '3840x720', '4098x768', '4800x900', '5760x1080', '6144x1152',
    '7200x1350', '7680x1440', '8640x1620', '10662x1999', '20', '11520x2160',
    '15360x2880', '23040x4320', '21', '3072x768', '3456x864', '3840x960',
    '4200x1050', '4320x1080', '4800x1200', '5040x1260', '5760x1440',
    '6144x1536', '7680x1920', '8400x2100', '9600x2400', '12288x3072',
    '19200x4800', '22', '3840x1024', '7680x2048', '11250x3000', '15360x4096',
    '23', '3456x768', '4320x960', '5760x1280', '6000x1333', '6480x1440',
    '8208x1824', '9000x2000')
CATEGORIES = (
    'aero', 'auroras', 'black', 'bokeh', 'colorful', 'creative', 'fresh',
    'macro', 'patterns', 'rainbow', 'vector_art', 'white', 'animals', 'birds',
    'horses', 'insects', 'others', 'pets', 'reptiles__frogs', 'sea', 'wild',
    'architecture', 'army', 'artistic', '3d', 'abstract', 'anime', 'drawings',
    'fantasy', 'graffiti', 'grunge', 'sculpture', 'typography', 'urban',
    'awareness', 'black_and_white', 'cartoons', 'bee_movie', 'bolt', 'brave',
    'cars', 'coraline', 'futurama', 'gnomeo__juliet', 'ice_age', 'incredibles',
    'kung_fu_panda', 'madagascar', 'monsters_inc', 'ninja_turtles',
    'old_disney', 'open_season', 'others_2', 'planet_51', 'ratatouille',
    'rick_and_morty', 'shrek', 'south_park', 'tangled',
    'the_princess_and_the_frog', 'the_simpsons', 'tinker_bell', 'toy_story',
    'up', 'walle', 'celebrities', 'models', 'movies_2', 'music_2', 'city',
    'computers', 'android', 'firefox', 'hardware', 'linux', 'mac', 'nvidia',
    'others_3', 'vaio', 'web', 'windows', 'cute', 'elements', 'earth', 'fire',
    'water', 'food_and_drink', 'funny', 'games', 'age_of_empires',
    'angry_birds', 'anno_1404', 'assassins_creed', 'avatar_2', 'batman_2',
    'battlefield', 'bioshock', 'brink', 'call_of_duty', 'chess',
    'command_and_conquer', 'counter_strike', 'crysis', 'dantes_inferno',
    'darksiders', 'dead_space', 'destiny', 'deus_ex', 'devil_may_cry', 'diablo',
    'dota', 'dragon_age', 'driver', 'empire_total_war', 'fable', 'fallout',
    'far_cry', 'fear', 'final_fantasy', 'fortnite', 'forza_motorsport',
    'gears_of_war', 'ghost_recon', 'god_of_war', 'gran_turismo',
    'grand_theft_auto', 'guild_wars', 'half_life', 'halo', 'heavenly_sword',
    'heroes', 'hitman', 'infamous', 'killzone', 'l_a__noire',
    'league_of_legends', 'left_4_dead', 'machinarium', 'mario', 'mass_effect',
    'medal_of_honor', 'metal_gear', 'midnight_club', 'minecraft',
    'mirrors_edge', 'mortal_kombat', 'need_for_speed', 'other_games',
    'overlord', 'poker', 'portal', 'prince_of_persia', 'prototype',
    'quake_wars', 'rayman', 'rayman_raving_rabbids', 'red_dead_redemption',
    'resident_evil', 'rift', 'rockstar_games', 's_t_a_l_k_e_r_',
    'splinter_cell', 'star_wars_2', 'starcraft', 'street_fighter',
    'the_elder_scrolls', 'the_witcher', 'thief', 'tom_clancy', 'tomb_raider',
    'trine', 'two_worlds', 'uncharted', 'valkyria_chronicles', 'warhammer',
    'watch_dogs', 'world_of_warcraft', 'girls', 'holidays', 'birthday',
    'childrens_day', 'christmas', 'easter', 'fathers_day', 'halloween',
    'independence_day', 'mothers_day', 'new_year', 'saint_patricks_day',
    'valentines_day', 'love', 'motors', 'airplane', 'atv', 'cars_2',
    'classic_cars', 'motorcycles', 'others_4', 'supercars_2', 'trains',
    'movies', '28_weeks_later', '300', 'alice_in_wonderland',
    'angels_and_demons', 'avatar', 'batman', 'captain_america',
    'clash_of_the_titans', 'game_of_thrones', 'harry_potter',
    'high_school_musical', 'hitman_2', 'iron_man', 'king_kong', 'lost',
    'man_of_steel', 'other_movies', 'oz_the_great_and_powerful',
    'pirates_of_the_caribbean', 'prince_of_persia_2', 'real_steel',
    'robin_hood', 'sex_and_the_city', 'snow_white__the_huntsman', 'spider_man',
    'star_trek', 'star_wars', 'sucker_punch', 'the_avengers', 'the_hobbit',
    'the_incredible_hulk', 'thor', 'transformers', 'tron_legacy', 'twilight',
    'watchmen', 'x_men', 'music', 'nature', 'beach', 'desert', 'flowers',
    'forests', 'lakes', 'landscape', 'mountains', 'rivers', 'sun__sky',
    'waterfalls', 'seasons', 'autumn', 'calendar', 'spring', 'summer', 'winter',
    'space', 'sports', '2016_summer_olympics', 'baseball', 'basketball',
    'biking', 'boxing', 'fitness', 'football', 'formula_1', 'free_running',
    'golf', 'motorcycle_racing', 'other_sports', 'parkour', 'skateboarding',
    'skiing', 'surfing', 'tennis', 'winter_olympic_games', 'wrestling',
    'travel', 'africa', 'america', 'antarctica', 'asia', 'europe', 'islands',
    'maps', 'oceania', 'other', 'vintage')

_ATTRS_RESOLUTIONS = {'id': 'wallpaper-resolutions'}


def _is_resolution(data: str) -> bool:
    return not data.isdigit()


def _get_resolution(ratios: list[str], quality: str, resolutions: sgml.Element) -> str:
    for ratio in ratios:
        if (header := resolutions.find('h3', text=ratio)) is not None:
            if quality == QUALITIES[0]:
                return header.get_next_sibling(1).get_data()
            else:
                return sgml.find_element(header.iter_next_siblings(
                ), 'br').get_previous_sibling().get_data()


class WallpapersWide(Source):
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORDER: list[str],
        CONFIG_QUALITY: str,
        CONFIG_GALLERY: str,
        CONFIG_SEARCH: str,
        CONFIG_RATIO: str,
        CONFIG_RESOLUTION: str,
        CONFIG_CATEGORY: str,
        CONFIG_RESOLUTIONS: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORDER: list(ORDER),
        CONFIG_QUALITY: QUALITIES[1],
        CONFIG_GALLERY: GALLERIES[0],
        CONFIG_SEARCH: '',
        CONFIG_RATIO: RATIOS[0],
        CONFIG_RESOLUTION: RESOLUTIONS[0],
        CONFIG_CATEGORY: CATEGORIES[0],
        CONFIG_RESOLUTIONS: RESOLUTIONS[28]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_unordered, CONFIG_ORDER, ORDER)
        cls._fix_config(validator.ensure_contains, CONFIG_QUALITY, QUALITIES)
        cls._fix_config(validator.ensure_contains, CONFIG_GALLERY, GALLERIES)
        cls._fix_config(validator.ensure_contains, CONFIG_RATIO, RATIOS)
        cls._fix_config(validator.ensure_contains, CONFIG_RESOLUTION, RESOLUTIONS)
        cls._fix_config(validator.ensure_truthy, CONFIG_RESOLUTION, _is_resolution)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_contains, CONFIG_RESOLUTIONS, RESOLUTIONS)
        cls._fix_config(validator.ensure_truthy, CONFIG_RESOLUTIONS)
        cls._fix_config(validator.ensure_truthy, CONFIG_RESOLUTIONS, _is_resolution)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        gui.add_menu_item(cls._text('LABEL_FILTER'), enable=False)
        item_resolution = gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {
            resolution: cls._text(f'RESOLUTION_{resolution}')
            for resolution in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION)
        menu_resolution = item_resolution.get_submenu()
        for resolution in menu_resolution:
            resolution.enable(_is_resolution(resolution.get_uid()))
        on_ratio = functools.partial(cls._on_ratio, item_resolution.enable)
        item_ratio = gui.add_submenu_radio(cls._text('MENU_RATIO'), {ratio: cls._text(
            f'RATIO_{ratio}') for ratio in RATIOS}, cls.CURRENT_CONFIG,
                                           CONFIG_RATIO, on_click=on_ratio, position=2)
        on_ratio(cls.CURRENT_CONFIG[CONFIG_RATIO])
        gui.add_menu_item(cls._text('LABEL_CLEAR'), on_click=functools.partial(
            cls._on_clear, item_ratio.get_submenu()[0], menu_resolution[0]))
        gui.add_separator()
        enable_category = gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {
            category: cls._text(f'CATEGORY_{category}')
            for category in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY).enable
        item_resolutions = gui.add_submenu_radio(cls._text('MENU_RESOLUTIONS'), {
            resolution: cls._text(f'RESOLUTION_{resolution}') for resolution
            in RESOLUTIONS[1:]}, cls.CURRENT_CONFIG, CONFIG_RESOLUTIONS)
        for resolution in item_resolutions.get_submenu():
            resolution.enable(_is_resolution(resolution.get_uid()))
        on_gallery = functools.partial(cls._on_gallery, enable_category, item_resolutions.enable)
        gui.add_submenu_radio(cls._text('MENU_GALLERY'), {
            gallery: cls._text(f'GALLERY_{gallery}') for gallery in GALLERIES},
                              cls.CURRENT_CONFIG, CONFIG_GALLERY, on_click=on_gallery, position=0)
        on_gallery(cls.CURRENT_CONFIG[CONFIG_GALLERY])
        gui.add_separator()
        gui.add_submenu_radio(cls._text('MENU_QUALITY'), {
            quality: cls._text(f'QUALITY_{quality}') for quality in QUALITIES},
                              cls.CURRENT_CONFIG, CONFIG_QUALITY)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        wallpapers = []
        gallery = params.pop(CONFIG_GALLERY)
        if gallery in GALLERIES[1:6]:
            url = request.join_url(URL_BASE, f'{gallery}_wallpapers')
        elif gallery == GALLERIES[6]:
            url = request.encode_params(URL_SEARCH, {CONFIG_SEARCH: params.pop(CONFIG_SEARCH)})
        elif gallery == GALLERIES[7]:
            url = request.join_url(URL_BASE, f'{params.pop(CONFIG_CATEGORY)}-desktop-wallpapers')
        elif gallery == GALLERIES[8]:
            url = request.join_url(URL_BASE, f'{params.pop(CONFIG_RESOLUTIONS)}-wallpapers-r')
        else:
            url = URL_BASE
        ratio = params.pop(CONFIG_RATIO)
        if ratio == RATIOS[0]:
            resolution = params.pop(CONFIG_RESOLUTION)
            data = {CONFIG_RESOLUTION: resolution} if resolution else {}
        else:
            data = {CONFIG_RATIO: ratio}
        session = request.Session()
        page = 1
        if data:
            while True:
                response = session.post(URL_FILTER, data=data)
                if response.status_code == request.Status.FOUND:
                    break
                yield
        while True:
            if not wallpapers:
                response = session.get(request.join_url(url, 'page', str(page)))
                if response:
                    html = sgml.loads(response.text)
                    wallpapers = list(html.find_all('div', classes='thumb'))
                    if html.find('a', text='Next »') is None:
                        page = 1
                    else:
                        page += 1
                if not wallpapers:
                    yield
                    continue
            wallpaper = wallpapers.pop(0)
            link = wallpaper[0][0]
            path = link['href']
            url_wallpaper = request.join_url(URL_BASE, path)
            response = session.get(url_wallpaper)
            if not response:
                wallpapers.insert(0, wallpaper)
                yield
                continue
            resolution = _get_resolution(cls.CURRENT_CONFIG[CONFIG_ORDER], cls.CURRENT_CONFIG[
                CONFIG_QUALITY], sgml.loads(response.text).find('div', _ATTRS_RESOLUTIONS))
            width, height = map(int, resolution.split('x'))
            yield ImageFile(request.join_url(URL_DOWNLOAD, f'{path[1:-6]}-{resolution}.jpg'),
                            f'{link[0].get_data()}.jpg', url=url_wallpaper, width=width, height=height)

    @staticmethod
    def _on_clear(item_ratio_: gui.MenuItem, item_resolution_: gui.MenuItem):
        item_ratio_.check()
        item_ratio_.trigger(gui.MenuItemEvent.LEFT_UP)
        item_resolution_.check()
        item_resolution_.trigger(gui.MenuItemEvent.LEFT_UP)

    @staticmethod
    def _on_ratio(enable_resolution: Callable[[bool], bool], ratio: str):
        enable_resolution(ratio == RATIOS[0])

    @staticmethod
    def _on_gallery(enable_category: Callable[[bool], bool],
                    enable_resolution: Callable[[bool], bool], gallery: str):
        enable_category(gallery == GALLERIES[7])
        enable_resolution(gallery == GALLERIES[8])
