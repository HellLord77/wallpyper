import configparser
import inspect
import os

_CONFIG_PATH = ''
_MODULES = ()

NAME = 'NAME'
MODULES = 'MODULES'
DEFAULT_CONFIG = 'DEFAULT_CONFIG'
CONFIG = 'CONFIG'
CONFIG_PATH = 'CONFIG_PATH'
INITIALIZED = False


def exists() -> bool:
    return INITIALIZED and os.path.isfile(CONFIG_PATH)


def load() -> bool:
    if INITIALIZED:
        config = configparser.ConfigParser()
        config.read(_CONFIG_PATH)
        for module in _MODULES:
            if config.has_section(module[NAME]):
                for key, value in module[DEFAULT_CONFIG].items():
                    module[CONFIG][key] = config.get(module[NAME], key, fallback=value)
            else:
                module[CONFIG].update(module[DEFAULT_CONFIG])
    return INITIALIZED


def save() -> bool:
    if INITIALIZED:
        config = configparser.ConfigParser()
        for module in _MODULES:
            config[module[NAME]] = module[CONFIG]
        with open(_CONFIG_PATH, 'w') as file:
            config.write(file)
    return INITIALIZED


def init() -> None:
    global _MODULES, _CONFIG_PATH, INITIALIZED
    main = inspect.stack()[-1].frame.f_globals
    _CONFIG_PATH = main[CONFIG_PATH]
    _MODULES = (main,) + tuple(module.__dict__ for module in main[MODULES])
    INITIALIZED = True
