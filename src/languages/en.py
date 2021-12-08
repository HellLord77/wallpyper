NEXT = 'Next Wallpaper'
PREVIOUS = 'Previous Wallpaper'
CHANGING = 'Changing Wallpaper'
FAILED_CHANGING = 'Failed Changing Wallpaper'
AUTO_CHANGE = 'Auto Change Wallpaper'
CHANGE_INTERVAL = 'Auto Change Interval'
SAVE = 'Save Wallpaper'
SAVING = 'Saving Wallpaper'
FAILED_SAVING = 'Failed Saving Wallpaper'
AUTO_SAVE = 'Auto Save Wallpaper'
MODIFY_SAVE = 'Modify Save Location'
SUBMENU_OPEN = 'Open Wallpaper'
OPEN_EXPLORER = 'In Explorer'
FAILED_OPENING_EXPLORER = 'Failed Opening Wallpaper in Explorer'
OPEN = 'With Default App'
FAILED_OPENING = 'Failed Opening Wallpaper with Default App'
SUBMENU_COPY = 'Copy to Clipboard'
COPY_PATH = 'Wallpaper Path'
FAILED_COPYING_PATH = 'Failed Copying Wallpaper Path to Clipboard'
COPY = 'Wallpaper Image'
FAILED_COPYING = 'Failed Copying Wallpaper Image to Clipboard'
SEARCH = 'Search Similar Wallpapers'
SEARCHING = 'Searching Similar Wallpapers'
FAILED_SEARCHING = 'Failed Searching Similar Wallpapers'
SUBMENU_ACTIONS = 'Additional Actions'
CLEAR = 'Clear Cache'
FAILED_CLEARING = 'Failed clearing cache'
RESTART = 'Restart Wallpyper'
SUBMENU_SETTINGS = 'Wallpyper Settings'
ANIMATE = 'Animate Tray Icon'
NOTIFY = 'Display Notifications'
KEEP_CACHE = 'Keep Wallpaper Cache'
AUTO_START = 'Start at System Startup'
KEEP_SETTINGS = 'Save Settings'
ABOUT = 'About Wallpyper'
QUIT = 'Quit Wallpyper'
FAILED_QUITING = 'Executing remaining tasks'


def __getattr__(name: str) -> str:
    return f'${name}'
